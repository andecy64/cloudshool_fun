import logging


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    s_handler = logging.StreamHandler()
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    s_handler.setFormatter(formatter)
    logger.addHandler(s_handler)
    return logger
