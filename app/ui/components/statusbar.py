from PySide6.QtWidgets import QStatusBar

class StatusBar(QStatusBar):
    def set_message(self, msg: str):
        self.showMessage(msg, 5000)
