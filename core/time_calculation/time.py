from time import time


class TimeCalculation(object):

    def __init__(self, function):

        self.function = function
        self.preparation = None

        self.__start_time = 0
        self.__stop_time = 0

        self.__time_min_resolution = 0
        self.__error_percentage = 5

        self.__execution_times = []

    def __tare_function(self, num_elements):
        array = self.preparation(num_elements)
        self.function(array)

    def time(self, num_elements, t_min):

        rip_tare = self.rip_calculation(t_min)
        rip_gross = self.rip_calculation(t_min)

        self.start()
        while range(rip_tare):
            e = self.preparation(d)

        self.stop()
        time_tare = self.result_time

        self.start()
        for (int i = 0; i < ripLordo; i++)
            e = prepara(n)
        self.stop()

        self.start()
        time_gross = self.result_time

        time_average = (time_gross / ripLordo) - (time_tare / ripTara);
        return time_average

    @property
    def result_time(self):
        return self.__stop_time - self.__start_time

    def start(self):
        self.__start_time = time()

    def stop(self):
        self.__stop_time = time()

    def reset(self):
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

    def rip_calculation(self, execute, t_min):

        iterations = 1
        self.reset()
        while self.result_time <= t_min:
            iterations *= 2
            self.start()
            while range(iterations):
                execute()
            self.stop()

        iter_max = iterations
        iter_min = iterations/2

        while iter_max - iter_min <= self.__error_percentage:
            iterations = (iter_max + iter_min)/2
            self.start()
            while range(iterations):
                execute()
            self.stop()

            if self.result_time <= t_min:
                iter_min = iterations
            else:
                iter_max = iterations

        return iter_max



