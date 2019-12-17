#!/usr/bin/env python
from core.lwm.lwm_naive import LowMedianWeightedNaive
from core.lwm.lwm import LowMedianWeighted
from core.util.read_input import read_input


def prod():

    array = read_input()
    if not array:
        return

    print('Input: ' + str(array))
    print()

    m_naive = LowMedianWeightedNaive()
    out_naive = m_naive.lwm_calculate(array)

    m = LowMedianWeighted()
    m.lwm(array, 0, len(array) - 1)

    print('lwm naive: {}'.format(out_naive))
    print('lwm: {}'.format(m.result))


def time_calculation():
    pass


def main():
    prod()


if __name__ == '__main__':
    main()
