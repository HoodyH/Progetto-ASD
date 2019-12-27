#!/usr/bin/env python
from core.config import *

from core.lwm.lwm_naive import LowMedianWeightedNaive
from core.lwm.lwm import LowMedianWeighted
from core.util.read_input import read_input

from core.time_calculation.execution_time import ExecutionTimeCalculation


def prod():

    array = read_input()
    if not array:
        return

    m_naive = LowMedianWeightedNaive()
    m_naive.lwm(array)

    m = LowMedianWeighted()
    m.lwm(array)

    print('lwm naive: {}'.format(m_naive.result))
    print('lwm: {}'.format(m.result))


def time_calculation():
    etc = ExecutionTimeCalculation()
    etc.multiple_time_calculation(t_start_value, t_increment, t_max_value)


def main():
    if execute_time_calculation:
        time_calculation()
    else:
        prod()


if __name__ == '__main__':
    main()
