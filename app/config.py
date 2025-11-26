import pathlib

APP_NAME = "Meta-Cell Chip Designer"
APP_VERSION = "1.0.0"

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
DATA_DIR = BASE_DIR / "data"

LOG_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)
