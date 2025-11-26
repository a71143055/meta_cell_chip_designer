from dataclasses import dataclass

@dataclass
class Primitive:
    kind: str  # e.g., "R", "C", "L", "CELL"
    value: float  # simplistic scalar parameter
