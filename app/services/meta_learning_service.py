from ..ml.meta_engine import MetaEngine
from ..ml.tasks import TargetWaveformTask

class MetaLearningService:
    def __init__(self, canvas, sim_service, logger):
        self.canvas = canvas
        self.sim = sim_service
        self.logger = logger
        self.engine = MetaEngine()

    def run_optimization(self, circuit):
        # Example task: tune primitive values to match target waveform amplitude
        task = TargetWaveformTask(target_amp=0.8)
        report = self.engine.optimize(circuit, self.sim.solver, task, steps=50)
        self.logger.info(f"Meta-learning report: {report}")
        return report
