from core.time_calculation.time import TimeCalculation
from core.time_calculation.generator import SeedGenerator


class ExecutionTimeCalculation(object):

    def __init__(self):

        self.execution_times = []

        # self.tc = TimeCalculation()

    def run(self):
        sg = SeedGenerator()
        out = sg.generate_array(10)
        print(out)
