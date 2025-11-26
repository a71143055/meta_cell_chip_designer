from dataclasses import dataclass

@dataclass
class Primitive:
    kind: str   # "R", "C", "L", "CELL"
    value: float
