from app.models.circuit import Circuit
from app.models.primitives import Primitive

def test_add_primitive():
    c = Circuit()
    c.add_primitive(Primitive("R", 10.0))
    assert len(c.primitives) == 1
    assert c.parameters()[0] == 10.0
