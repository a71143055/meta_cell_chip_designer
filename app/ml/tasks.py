import numpy as np
from .datasets import synthetic_waveform

class TargetWaveformTask:
    def __init__(self, target_amp: float):
        self.target_amp = target_amp
        self.x, self.y = synthetic_waveform(amp=target_amp)

    def loss(self, sim_output):
        # Mean squared error between simulated amplitude and target amplitude
        target_amp = self.target_amp
        sim_amp = np.clip(sim_output.get("amplitude", 0.0), 0.0, 10.0)
        return float((sim_amp - target_amp) ** 2)
