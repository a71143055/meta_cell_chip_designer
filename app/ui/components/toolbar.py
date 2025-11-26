from PySide6.QtWidgets import QToolBar, QPushButton

class MainToolbar(QToolBar):
    def __init__(self):
        super().__init__("Tools")
        self.add_resistor = QPushButton("Add R")
        self.add_capacitor = QPushButton("Add C")
        self.add_inductor = QPushButton("Add L")
        self.add_cell = QPushButton("Add CELL")
        for b in [self.add_resistor, self.add_capacitor, self.add_inductor, self.add_cell]:
            self.addWidget(b)
