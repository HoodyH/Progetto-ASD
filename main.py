#!/usr/bin/env python
from config import (execute_time_calculation)

from core.lwm.lwm_naive import LowMedianWeightedNaive
from core.lwm.lwm import LowMedianWeighted
from core.util.read_input import read_input

from core.time_calculation.execution_time import ExecutionTimeCalculation


def prod():

    array = read_input()
    if not array:
        return

    m_naive = LowMedianWeightedNaive()
    out_naive = m_naive.lwm_calculate(array)

    m = LowMedianWeighted()
    m.lwm(array, 0, len(array) - 1)

    print('lwm naive: {}'.format(out_naive))
    print('lwm: {}'.format(m.result))


def time_calculation():
    etc = ExecutionTimeCalculation()
    etc.run()


def main():
    if execute_time_calculation:
        time_calculation()
    else:
        prod()


if __name__ == '__main__':
    main()
