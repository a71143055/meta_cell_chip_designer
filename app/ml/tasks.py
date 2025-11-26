import numpy as np

class TargetWaveformTask:
    def __init__(self, target_amp: float):
        self.target_amp = float(target_amp)

    def loss(self, sim_output: dict) -> float:
        sim_amp = float(sim_output.get("amplitude", 0.0))
        return float((sim_amp - self.target_amp) ** 2)
