from core.serialization import save_project, load_project
from simulation.spice_export import export_spice

class ProjectService:
    def __init__(self, canvas, inspector, logger):
        self.canvas = canvas
        self.inspector = inspector
        self.logger = logger

    def save(self, path: str) -> bool:
        try:
            save_project(self.canvas.circuit, path)
            self.logger.info(f"Saved project: {path}")
            return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def load(self, path: str) -> bool:
        try:
            circuit = load_project(path)
            self.canvas.circuit = circuit
            self.logger.info(f"Loaded project: {path}")
            self.canvas.update()
            return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def export_spice(self, path: str) -> bool:
        try:
            export_spice(self.canvas.circuit, path)
            self.logger.info(f"Exported SPICE: {path}")
            return True
        except Exception as e:
            self.logger.exception(e)
            return False
