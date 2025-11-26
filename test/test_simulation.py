from app.models.circuit import Circuit
from app.models.primitives import Primitive
from simulation.solver import SimpleSolver

def test_dc_solver():
    c = Circuit()
    for _ in range(3):
        c.add_primitive(Primitive("R", 10.0))
    s = SimpleSolver()
    res = s.solve_dc(c)
    assert "DC amplitude" in res.summary()
