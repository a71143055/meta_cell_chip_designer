from app.models.circuit import Circuit

def export_spice(circuit: Circuit, path: str):
    lines = ["* Meta-Cell Chip Designer SPICE export"]
    for i, p in enumerate(circuit.primitives, start=1):
        if p.kind == "R":
            lines.append(f"R{i} n{i} n{i+1} {p.value}")
        elif p.kind == "C":
            lines.append(f"C{i} n{i} n{i+1} {p.value}")
        elif p.kind == "L":
            lines.append(f"L{i} n{i} n{i+1} {p.value}")
        elif p.kind == "CELL":
            lines.append(f"X{i} n{i} n{i+1} meta_cell value={p.value}")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
