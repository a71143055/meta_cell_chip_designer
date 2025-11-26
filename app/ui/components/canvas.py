from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt, QPoint
from ...models.circuit import Circuit
from ...models.primitives import Primitive

class CircuitCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.circuit = Circuit()
        self.setMouseTracking(True)

    def add_primitive(self, kind: str):
        p = Primitive(kind=kind, value=1.0)
        self.circuit.add_primitive(p)
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.fillRect(self.rect(), QColor("#1e1e1e"))
        qp.setPen(QPen(QColor("#cccccc"), 1))
        x, y = 40, 40
        for i, prim in enumerate(self.circuit.primitives):
            qp.setPen(QPen(QColor("#86c"), 2))
            qp.drawRect(x, y + i * 50, 100, 30)
            qp.setPen(QPen(QColor("#fff"), 1))
            qp.drawText(QPoint(x + 10, y + i * 50 + 20), f"{prim.kind}={prim.value:.2f}")
