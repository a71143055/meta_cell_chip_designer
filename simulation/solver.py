import numpy as np
from dataclasses import dataclass

@dataclass
class SimResult:
    amplitude: float

    def summary(self) -> str:
        return f"DC amplitude={self.amplitude:.3f}"

class SimpleSolver:
    def solve_dc(self, circuit):
        vals = np.array(circuit.parameters(), dtype=float)
        if vals.size == 0:
            amp = 0.0
        else:
            amp = float(np.tanh(vals.sum() / (len(vals) + 1.0)))
        return SimResult(amplitude=amp)

    def evaluate_amplitude(self, circuit):
        res = self.solve_dc(circuit)
        return {"amplitude": res.amplitude}
