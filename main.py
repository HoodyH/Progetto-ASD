#!/usr/bin/env python
from core.config import debug_check
from core.lwm.lwm import LowMedianWeighted
from core.util.read_input import read_input


def prod():

    debug_check()

    array = read_input()
    if not array:
        return

    m = LowMedianWeighted()
    m.lwm(array)

    print('{}'.format(m.result))


def main():
    prod()


if __name__ == '__main__':
    main()
