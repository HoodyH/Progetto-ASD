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

        self.m = LowMedianWeighted()
        self.m_naive = LowMedianWeightedNaive()

    def single_time_calculation(self, array_len):

        time, delta = self.tc.measure(
            self.rg.generate_array,
            self.m.lwm,
            array_len,
            10,
            1.96,
            self.tc.calculate_time_min_resolution(),
            sys.float_info.max,
        )
        return time, delta

    def multiple_time_calculation(self, array_len_start, increment, max_value):

        out = []
        array_len = array_len_start

        while array_len < max_value:

            c = 10
            za = 1.96

            print('Calculating for {} elements...'.format(array_len))
            time, delta = self.tc.measure(
                self.rg.generate_array,
                self.m.lwm,
                array_len,
                c,
                za,
                self.tc.calculate_time_min_resolution(),
                sys.float_info.max,
            )

            print('{} el time: {}, delta: {}\n'.format(array_len, time, delta))
            out.append((increment, time, delta))
            array_len += increment

        return out
