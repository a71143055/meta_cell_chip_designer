import numpy as np

class MetaEngine:
    def optimize(self, circuit, solver, task, steps=100, lr=0.05):
        params = np.array(circuit.parameters(), dtype=float)
        if params.size == 0:
            return {"status": "no-params"}

        history = []
        for _ in range(steps):
            loss = task.loss(solver.evaluate_amplitude(circuit))
            grad = self._estimate_grad(circuit, solver, task, params)
            params -= lr * grad
            params = np.clip(params, 0.0, 1000.0)
            circuit.set_parameters(params.tolist())
            history.append(float(loss))

        return {"final_loss": float(history[-1]), "steps": steps}

    def _estimate_grad(self, circuit, solver, task, params, epsilon=1e-2):
        grad = []
        for i in range(len(params)):
            backup = params[i]

            params[i] = backup + epsilon
            circuit.set_parameters(params.tolist())
            loss_plus = task.loss(solver.evaluate_amplitude(circuit))

            params[i] = backup - epsilon
            circuit.set_parameters(params.tolist())
            loss_minus = task.loss(solver.evaluate_amplitude(circuit))

            params[i] = backup
            circuit.set_parameters(params.tolist())

            g = (loss_plus - loss_minus) / (2 * epsilon)
            grad.append(g)

        return np.array(grad, dtype=float)
