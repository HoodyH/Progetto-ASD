#!/usr/bin/env python
from core.lwm.lwm import LowMedianWeighted
from core.lwm.lwm_naive import LowMedianWeightedNaive
from core.util.read_input import read_input


def prod():

    array = read_input()
    if not array:
        return

    m = LowMedianWeighted()
    m = LowMedianWeightedNaive()
    m.lwm(array)

    print('{}'.format(m.result))


def main():
    prod()


if __name__ == '__main__':
    main()
