from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from .components.canvas import CircuitCanvas
from .components.toolbar import MainToolbar
from .components.inspector import InspectorPanel
from .components.statusbar import StatusBar
from ..services.project_service import ProjectService
from ..services.simulation_service import SimulationService
from ..services.meta_learning_service import MetaLearningService

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

    def _init_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        open_act = QAction("Open Project", self)
        save_act = QAction("Save Project", self)
        export_act = QAction("Export SPICE", self)
        file_menu.addAction(open_act)
        file_menu.addAction(save_act)
        file_menu.addAction(export_act)
        self.open_act = open_act
        self.save_act = save_act
        self.export_act = export_act

        run_menu = menu.addMenu("Run")
        sim_act = QAction("Run Simulation", self)
        meta_act = QAction("Run Meta-Learning", self)
        run_menu.addAction(sim_act)
        run_menu.addAction(meta_act)
        self.sim_act = sim_act
        self.meta_act = meta_act

    def _connect(self):
        self.open_act.triggered.connect(self._on_open)
        self.save_act.triggered.connect(self._on_save)
        self.export_act.triggered.connect(self._on_export)
        self.sim_act.triggered.connect(self._on_simulate)
        self.meta_act.triggered.connect(self._on_meta)

        self.toolbar.add_resistor.clicked.connect(lambda: self.canvas.add_primitive("R"))
        self.toolbar.add_capacitor.clicked.connect(lambda: self.canvas.add_primitive("C"))
        self.toolbar.add_inductor.clicked.connect(lambda: self.canvas.add_primitive("L"))
        self.toolbar.add_cell.clicked.connect(lambda: self.canvas.add_primitive("CELL"))

    def _on_open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open", filter="Project (*.mccproj)")
        if path:
            ok = self.project.load(path)
            if not ok:
                QMessageBox.warning(self, "Open Failed", "Could not open project.")

    def _on_save(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save", filter="Project (*.mccproj)")
        if path:
            ok = self.project.save(path)
            if not ok:
                QMessageBox.warning(self, "Save Failed", "Could not save project.")

    def _on_export(self):
        path, _ = QFileDialog.getSaveFileName(self, "Export SPICE", filter="SPICE (*.cir)")
        if path:
            ok = self.project.export_spice(path)
            if not ok:
                QMessageBox.warning(self, "Export Failed", "Could not export SPICE.")

    def _on_simulate(self):
        result = self.sim.run(self.canvas.circuit)
        self.status.set_message(f"Sim result: {result.summary()}")

    def _on_meta(self):
        report = self.meta.run_optimization(self.canvas.circuit)
        self.status.set_message(f"Meta-learning complete: {report}")
