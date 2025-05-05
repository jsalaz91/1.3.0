import logging

def gift_ore(amount):
    logging.info(f"Gifting {amount} ORE tokens to reward wallet.")

def simulate_gift():
    for amt in [10, 25, 50]:
        gift_ore(amt)
