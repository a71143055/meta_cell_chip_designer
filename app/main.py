import sys
from PySide6.QtWidgets import QApplication
from .logging_conf import init_logging
from .ui.main_window import MainWindow

def main():
    logger = init_logging()
    app = QApplication(sys.argv)
    win = MainWindow(logger=logger)
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
