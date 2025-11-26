from app.models.primitives import Primitive

class Circuit:
    def __init__(self):
        self.primitives: list[Primitive] = []

    def add_primitive(self, prim: Primitive):
        self.primitives.append(prim)

    def parameters(self):
        return [p.value for p in self.primitives]

    def set_parameters(self, vals):
        for p, v in zip(self.primitives, vals):
            p.value = float(v)
