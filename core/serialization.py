import json
from app.models.circuit import Circuit
from app.models.primitives import Primitive

def save_project(circuit: Circuit, path: str):
    data = [{"kind": p.kind, "value": p.value} for p in circuit.primitives]
    with open(path, "w", encoding="utf-8") as f:
        f.write(json.dumps({"primitives": data}))

def load_project(path: str) -> Circuit:
    with open(path, "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    c = Circuit()
    for item in data.get("primitives", []):
        c.add_primitive(Primitive(kind=item["kind"], value=float(item["value"])))
    return c
