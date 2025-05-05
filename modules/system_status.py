import asyncio
import logging
import psutil

def log_system_status():
    try:
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        # Only log if accessible
        if cpu is not None and mem is not None:
            logging.info(f"System Status - CPU: {cpu}%, Memory: {mem}%")
    except Exception:
        pass  # Silent fail on permission errors

async def monitor_system(interval=60):
    while True:
        log_system_status()
        await asyncio.sleep(interval)
