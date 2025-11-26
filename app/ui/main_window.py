from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from app.ui.components.canvas import CircuitCanvas
from app.ui.components.toolbar import MainToolbar
from app.ui.components.inspector import InspectorPanel
from app.ui.components.statusbar import StatusBar
from app.services.project_service import ProjectService
from app.services.simulation_service import SimulationService
from app.services.meta_learning_service import MetaLearningService

class MainWindow(QMainWindow):
    def __init__(self, logger):
        super().__init__()
        self.logger = logger
        self.setWindowTitle("Meta-Cell Chip Designer")
        self.resize(1200, 800)

        self.canvas = CircuitCanvas()
        self.toolbar = MainToolbar()
        self.inspector = InspectorPanel()
        self.status = StatusBar()
        self.setCentralWidget(self.canvas)
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)
        self.addDockWidget(Qt.RightDockWidgetArea, self.inspector.dock)
        self.setStatusBar(self.status)

        self.project = ProjectService(self.canvas, self.inspector, logger)
        self.sim = SimulationService(logger)
        self.meta = MetaLearningService(self.canvas, self.sim, logger)

        self._init_menu()
        self._connect()
    ...
