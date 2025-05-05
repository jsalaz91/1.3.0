import logging

halt_flag = False

def halt_trading():
    global halt_flag
    halt_flag = True
    logging.warning("Trading halted by halt_manager.")

def resume_trading():
    global halt_flag
    halt_flag = False
    logging.info("Trading resumed.")

def is_trading_halted():
    return halt_flag
