#!/usr/bin/env python
from time import time
from core.config import *

from core.lwm.lwm_insertion import LowMedianWeightedInsertion
from core.lwm.lwm_merge import LowMedianWeightedMerge
from core.lwm.lwm_linear import LowMedianWeightedLinear
from core.lwm.lwm_median_approx import LowMedianWeightedMedianApprox
from core.lwm.lwm import LowMedianWeighted

from core.util.read_input import read_input

from core.time_calculation.execution_time import ExecutionTimeCalculation


def get_algorithm():

    if exec_function is LWM_INSERTION:
        print('Executing Insertion')
        m = LowMedianWeightedInsertion()

    elif exec_function is LWM_LINEAR:
        print('Executing lwm_linear')
        m = LowMedianWeightedLinear()

    elif exec_function is LWM_MEDIAN_APPROX:
        print('Executing lwm_median_approx')
        m = LowMedianWeightedMedianApprox()

    elif exec_function is LWM:
        print('Executing lwm')
        m = LowMedianWeighted()

    else:
        print('Executing lwm_merge')
        m = LowMedianWeightedMerge()

    return m


def prod():

    array = read_input()
    if not array:
        return

    m_naive = LowMedianWeightedMerge()
    m = get_algorithm()

    m_naive.lwm(array)

    t1 = time()
    m.lwm(array)
    t = (time() - t1)/1000
    print('result: {} in {} sec'.format(m.result, t))
    if m_naive.result is m.result:
        print('PASS')
    else:
        print('FAIL')
        print('Right Value: {}'.format(m_naive.result))


def time_calculation():

    m = get_algorithm()

    etc = ExecutionTimeCalculation(m.lwm)
    out = etc.multiple_time_calculation(t_start_value, t_increment, t_max_value)
    for el in out:
        time_array_len, time, delta = el
        print('{};{};{}'.format(
            time_array_len,
            str(time).replace('.', ','),
            str(delta).replace('.', ',')
        ))


def main():

    debug_check()

    if execute_time_calculation:
        time_calculation()
    else:
        prod()


if __name__ == '__main__':
    main()
