import logging
from logging.handlers import RotatingFileHandler
from .config import LOG_DIR, APP_NAME

def init_logging():
    logger = logging.getLogger(APP_NAME)
    logger.setLevel(logging.INFO)
    fh = RotatingFileHandler(LOG_DIR / "app.log", maxBytes=1_000_000, backupCount=3, encoding="utf-8")
    sh = logging.StreamHandler()
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    fh.setFormatter(fmt)
    sh.setFormatter(fmt)
    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger
