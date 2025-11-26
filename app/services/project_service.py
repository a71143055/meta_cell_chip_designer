import json
from app.models.circuit import Circuit
from app.models.primitives import Primitive
from simulation.spice_export import export_spice

class ProjectService:
    def __init__(self, canvas, inspector, logger):
        self.canvas = canvas
        self.inspector = inspector
        self.logger = logger

    def save(self, path: str) -> bool:
        try:
            data = [{"kind": p.kind, "value": p.value} for p in self.canvas.circuit.primitives]
            with open(path, "w", encoding="utf-8") as f:
                json.dump({"primitives": data}, f, ensure_ascii=False, indent=2)
            self.logger.info(f"Saved project: {path}")
            return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def load(self, path: str) -> bool:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            c = Circuit()
            for item in data.get("primitives", []):
                c.add_primitive(Primitive(kind=item["kind"], value=float(item["value"])))
            self.canvas.circuit = c
            self.canvas.update()
            self.logger.info(f"Loaded project: {path}")
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
