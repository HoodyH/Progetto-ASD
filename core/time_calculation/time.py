from time import time


class TimeCalculation(object):

    def __init__(self):

        self.__start_time = 0
        self.__stop_time = 0

    @property
    def time(self):
        return time()

    def start(self):
        self.__start_time = self.time

    def stop(self):
        self.__stop_time = self.time

    @property
    def result(self):
        return self.__stop_time - self.__start_time
