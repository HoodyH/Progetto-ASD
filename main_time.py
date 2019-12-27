from core.time_calculation.execution_time import ExecutionTimeCalculation


def time_calculation():

    array_len = 1000
    etc = ExecutionTimeCalculation()

    calc = True  # change this value to switch to automate time calculation

    if calc:
        time, delta = etc.single_time_calculation(array_len)
        print('{} el time: {}, delta: {}\n'.format(array_len, time, delta))
    else:
        out = etc.multiple_time_calculation(array_len, 1000, 20000)
        for el in out:
            time_array_len, time, delta = el
            print('{} el time: {}, delta: {}\n'.format(time_array_len, time, delta))


def main():
    time_calculation()


if __name__ == '__main__':
    main()
