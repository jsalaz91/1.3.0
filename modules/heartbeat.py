import asyncio
import logging

async def heartbeat(interval=30):
    logging.info("Heartbeat: bot is alive.")
    await asyncio.sleep(interval)
