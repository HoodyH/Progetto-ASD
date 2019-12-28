import sys

from core.util.debug import debug

from core.lwm.lwm_naive import LowMedianWeightedNaive
from core.lwm.lwm import LowMedianWeighted

from core.time_calculation.time_calculation import TimeCalculation
from core.time_calculation.rand_generator import RandGenerator


class ExecutionTimeCalculation(object):

    def __init__(self):

        self.execution_times = []

        self.tc = TimeCalculation()
        self.rg = RandGenerator()

        self.c = 10
        self.za = 1.96

        m = LowMedianWeighted()
        m_naive = LowMedianWeightedNaive()
        self.function = m_naive.lwm

    def single_time_calculation(self, array_len):

        time, delta = self.tc.measure(
            self.rg.generate_array,
            self.function,
            array_len,
            self.c,
            self.za,
            self.tc.calculate_time_min_resolution(),
            sys.float_info.max,
        )
        return time, delta

    def multiple_time_calculation(self, array_len_start, increment, max_value):

        out = []
        array_len = array_len_start

        while array_len < max_value:

            debug('Calculating for {} elements...'.format(array_len))
            time, delta = self.tc.measure(
                self.rg.generate_array,
                self.function,
                array_len,
                self.c,
                self.za,
                self.tc.calculate_time_min_resolution(),
                sys.float_info.max,
            )
            debug('{} el time: {}, delta: {}\n'.format(
                array_len,
                str(time).replace('.', ','),
                str(delta).replace('.', ',')
            ))
            out.append((increment, time, delta))
            array_len += increment

        return out
