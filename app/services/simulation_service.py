from simulation.solver import SimpleSolver

class SimulationService:
    def __init__(self, logger):
        self.logger = logger
        self.solver = SimpleSolver()

    def run(self, circuit):
        result = self.solver.solve_dc(circuit)
        self.logger.info(result.summary())
        return result
from simulation.solver import SimpleSolver

class SimulationService:
    def __init__(self, logger):
        self.logger = logger
        self.solver = SimpleSolver()

    def run(self, circuit):
        result = self.solver.solve_dc(circuit)
        self.logger.info(result.summary())
        return result
