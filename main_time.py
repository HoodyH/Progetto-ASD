from core.config import debug_check

from core.time_calculation.execution_time import ExecutionTimeCalculation
from core.lwm.lwm import LowMedianWeighted


def time_calculation():
    debug_check()

    m = LowMedianWeighted()

    array_len = 1000
    etc = ExecutionTimeCalculation(m.lwm)

    time, delta = etc.single_time_calculation(array_len)
    print('{} el time: {}, delta: {}\n'.format(
        array_len,
        str(time).replace('.', ','),
        str(delta).replace('.', ',')
    ))


def main():
    time_calculation()


if __name__ == '__main__':
    main()
