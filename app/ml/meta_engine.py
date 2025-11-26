import numpy as np
from ..models.constraints import clamp_params

class MetaEngine:
    def optimize(self, circuit, solver, task, steps=100, lr=0.05):
        params = np.array(circuit.parameters(), dtype=float)
        if params.size == 0:
            return {"status": "no-params"}
        history = []
        for t in range(steps):
            sim_output = solver.evaluate_amplitude(circuit)
            loss = task.loss(sim_output)
            grad = self._estimate_grad(circuit, solver, task, params)
            params -= lr * grad
            params = np.array(clamp_params(params.tolist(), 0.0, 1000.0))
            circuit.set_parameters(params.tolist())
            history.append(float(loss))
        return {"final_loss": float(history[-1]), "steps": steps}

    def _estimate_grad(self, circuit, solver, task, params, epsilon=1e-2):
        grad = []
        base = task.loss(solver.evaluate_amplitude(circuit))
        for i in range(len(params)):
            backup = params[i]
            params[i] = backup + epsilon
            circuit.set_parameters(params.tolist())
            plus = task.loss(solver.evaluate_amplitude(circuit))
            params[i] = backup - epsilon
            circuit.set_parameters(params.tolist())
            minus = task.loss(solver.evaluate_amplitude(circuit))
            params[i] = backup
            circuit.set_parameters(params.tolist())
            g = (plus - minus) / (2 * epsilon)
            grad.append(g)
        return np.array(grad, dtype=float)
