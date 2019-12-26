from core.time_calculation.execution_time import ExecutionTimeCalculation


def time_calculation():
    etc = ExecutionTimeCalculation()
    etc.run()


def main():
    time_calculation()


if __name__ == '__main__':
    main()
