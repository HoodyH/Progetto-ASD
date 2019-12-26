import sys

from core.lwm.lwm_naive import LowMedianWeightedNaive
from core.lwm.lwm import LowMedianWeighted

from core.time_calculation.time_calculation import TimeCalculation
from core.time_calculation.rand_generator import RandGenerator


class ExecutionTimeCalculation(object):

    def __init__(self):

        self.execution_times = []

        self.tc = TimeCalculation()
        self.rg = RandGenerator()

    def run(self):

        m = LowMedianWeighted()
        array_len = 12000

        for i in range(0, 20):

            c = 10

            print('Calculating for {} elements...'.format(array_len))
            time = self.tc.measure(
                self.rg.generate_array,
                m.lwm,
                array_len,
                c,
                self.tc.calculate_time_min_resolution(),
                sys.float_info.max,
            )

            print('{} el time: {}\n'.format(array_len, time))
            array_len += 1000
