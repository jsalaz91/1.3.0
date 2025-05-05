import asyncio
import logging
import os
import traceback
import zipfile
import sys
from datetime import datetime
from multiprocessing import Process

from modules import toggle_settings, heartbeat, system_status, simulator

# Detect CLI mode
CLI_MODE = "--cli" in sys.argv
if not CLI_MODE:
    from modules import dashboard_gui

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[
                        logging.StreamHandler(),
                        logging.FileHandler("phase13_runtime.log", mode='a')
                    ])

def create_backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"phase13_backup_{timestamp}.zip"
    with zipfile.ZipFile(backup_name, 'w') as z:
        for fname in ["phase13_runtime.log", "data/settings.json"]:
            if os.path.exists(fname):
                z.write(fname)
    logging.info(f"Backup created: {backup_name}")

# Async task wrappers
async def heartbeat_task():
    while True:
        await heartbeat.heartbeat(interval=30)

async def system_monitor_task():
    while True:
        await system_status.monitor_system(interval=60)

async def trading_task():
    await simulator.simulate_trading(interval=10)

def launch_dashboard():
    dashboard_gui.launch_dashboard()

# Async orchestrator
async def main():
    toggle_settings.load_settings()
    dashboard_proc = None

    if not CLI_MODE:
        dashboard_proc = Process(target=launch_dashboard)
        dashboard_proc.start()

    try:
        await asyncio.gather(
            heartbeat_task(),
            system_monitor_task(),
            trading_task()
        )
    except Exception:
        logging.error("Main loop crashed:")
        logging.error(traceback.format_exc())
    finally:
        if dashboard_proc:
            dashboard_proc.terminate()
            dashboard_proc.join()

# Async-safe entrypoint
if __name__ == "__main__":
    restart_count = 0
    while True:
        mode = "CLI" if CLI_MODE else "FULL"
        logging.info(f"[RUN #{restart_count}] Starting Phase 13 ({mode}) mode")
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            logging.info("Shutdown requested by user.")
            break
        except Exception as e:
            logging.error("Unhandled crash. Restarting...")
            logging.error(traceback.format_exc())
        restart_count += 1
