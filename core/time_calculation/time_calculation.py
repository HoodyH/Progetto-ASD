from time import time
import math


class TimeCalculation(object):

    def __init__(self):

        self.__start_time = 0
        self.__stop_time = 0

        self.__error_percentage = 5

    @property
    def __result_time(self):
        return self.__stop_time - self.__start_time

    def __start(self):
        self.__start_time = time()

    def __stop(self):
        self.__stop_time = time()

    def __reset(self):
        self.__start_time = 0
        self.__stop_time = 0

    @staticmethod
    def __granularity():
        t0 = time()
        t1 = time()
        while t0 is t1:
            t1 = time()
        return t0 - t1

    def calculate_time_min_resolution(self):
        return self.__granularity() * 20

    @staticmethod
    def __execute(function_container, d):
        if isinstance(function_container, tuple):
            e = function_container[0](d)
            function_container[1](e)
        else:
            e = function_container(d)

    def __rip_calculation(self, function_container, d, t_min):

        iterations = 1
        self.__reset()
        while self.__result_time <= t_min:
            iterations *= 2
            self.__start()
            for i in range(int(iterations)):
                self.__execute(function_container, d)
            self.__stop()

        iter_max = iterations
        iter_min = iterations/2

        while iter_max - iter_min >= self.__error_percentage:
            iterations = (iter_max + iter_min)/2
            self.__start()
            for i in range(int(iterations)):
                self.__execute(function_container, d)
            self.__stop()

            if self.__result_time <= t_min:
                iter_min = iterations
            else:
                iter_max = iterations

        return iter_max

    def __average_net_time(self, prepare_f, main_f, d, t_min):

        rip_tare = self.__rip_calculation(prepare_f, d, t_min)
        rip_gross = self.__rip_calculation((prepare_f, main_f), d, t_min)

        self.__start()
        for i in range(int(rip_tare)):
            e = prepare_f(d)
        self.__stop()
        time_tare = self.__result_time

        self.__start()
        for i in range(int(rip_tare)):
            e = prepare_f(d)
            main_f(e)
        self.__stop()
        time_gross = self.__result_time

        time_average = (time_gross / rip_gross) - (time_tare / rip_tare)
        return time_average

    def measure(self, prepare_f, main_f, d, c, t_min, delta):
        t = 0
        sum_2 = 0
        cn = 0
        e = 0

        while not delta < (e/20):
            for i in range(1, c):
                m = self.__average_net_time(prepare_f, main_f, d, t_min)
                t = t + m
                sum_2 += (m * m)

            cn += c
            e = t / cn
            s = math.sqrt(sum_2 / cn - (e * e))
            delta = (1 / math.sqrt(cn)) * s * 1.96

        return e
