import asyncio
import logging
import random

async def simulate_trading(interval=6):
    order_id = 0
    while True:
        side = random.choice(['buy', 'sell'])
        price = round(100 + random.uniform(-3, 3), 2)
        volume = random.randint(10, 500)
        logging.info(f"[TRADE INTENT] {side.upper()} {volume} @ ${price} [order_id={order_id}]")
        order_id += 1
        await asyncio.sleep(interval)
