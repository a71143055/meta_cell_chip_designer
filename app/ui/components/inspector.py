from PySide6.QtWidgets import QWidget, QDockWidget, QVBoxLayout, QLabel, QSpinBox

class InspectorPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Inspector"))
        self.value_box = QSpinBox()
        self.value_box.setRange(0, 1000)
        layout.addWidget(self.value_box)

        self.dock = QDockWidget("Inspector")
        self.dock.setWidget(self)

