#!/usr/bin/env python
from core.config import *

from core.lwm.lwm_naive import LowMedianWeightedNaive
from core.lwm.lwm import LowMedianWeighted
from core.lwm.lwm_approx import LowMedianWeightedApprox

from core.util.read_input import read_input

from core.time_calculation.execution_time import ExecutionTimeCalculation


def prod():

    array = read_input()
    if not array:
        return

    m_naive = LowMedianWeightedNaive()
    m_naive.lwm(array)

    if exec_function is 2:
        print('Executing lwm_approx')
        m = LowMedianWeightedApprox()
        m.lwm(array)
        print('lwm_approx: {}'.format(m.result))
    else:
        print('Executing lwm')
        m = LowMedianWeighted()
        m.lwm(array)
        print('lwm: {}'.format(m.result))

    if m_naive.result is m.result:
        print('PASS')
    else:
        print('FAIL')
        print('Right Value: {}'.format(m_naive.result))


def time_calculation():
    m = LowMedianWeighted()
    m_naive = LowMedianWeightedNaive()
    m_approx = LowMedianWeightedApprox()

    if exec_function is 0:
        etc = ExecutionTimeCalculation(m_naive.lwm)
    elif exec_function is 2:
        etc = ExecutionTimeCalculation(m_approx.lwm)
    else:
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
    if execute_time_calculation:
        time_calculation()
    else:
        prod()


if __name__ == '__main__':
    main()
