from app.models.circuit import Circuit
from app.models.primitives import Primitive
from app.ml.meta_engine import MetaEngine
from app.ml.tasks import TargetWaveformTask
from simulation.solver import SimpleSolver

def test_meta_runs():
    c = Circuit()
    c.add_primitive(Primitive("R", 0.1))
    c.add_primitive(Primitive("C", 0.2))
    solver = SimpleSolver()
    engine = MetaEngine()
    task = TargetWaveformTask(target_amp=0.5)
    report = engine.optimize(c, solver, task, steps=5)
    assert "final_loss" in report
