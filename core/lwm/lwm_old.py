import math


class LowMedianWeighted(object):

    def __init__(self):
        self.array = []
        self.sum_array = None
        """
        Per salvare la somma ad ogni ciclo
        evitando di ricalcolare completamente.
        """
        self.sum_left = None
        self.sum_right = None

        self.idx_median = None

    @property
    def result(self):
        if self.idx_median:
            return self.array[self.idx_median]
        else:
            return 0

    def lwm_calculate(self, array, left, right):
        """
        Metodo che esegue il calcolo della mediana pesata inferiore
        :param array: array di input.
        :param left: primo valore utile dell'array
        :param right: ultimo valore utile dell'array
        :return: la mediana pesata inferiore
        """
        self.array = array
        self.sum_array = sum(array)
        if self.sum_array is 0:
            return 0

        idx_pivot = self.__median_of_medians(left, right)
        self.idx_median = self.__partition3(left, right, idx_pivot)

        left_array = self.array[:self.idx_median]
        self.sum_left = sum(left_array)
        right_array = self.array[self.idx_median:]
        self.sum_right = sum(right_array)

        return self.__lwm_loop(left, right)

    def __lwm_loop(self, left, right):

        h_sum = self.sum_array / 2

        left_array = self.array[:self.idx_median]
        print(left_array)
        right_array = self.array[self.idx_median:]
        print(right_array)

        print('idx median: {} --> S_left: {} < {} S_right: {} <= {}'.format(
            self.idx_median,
            self.sum_left,
            h_sum,
            self.sum_right,
            h_sum,
        ))
        print()

        if self.sum_left < h_sum and self.sum_right <= h_sum:
            return self.array[self.idx_median]

        elif self.sum_left >= h_sum:
            idx_prev_median = self.idx_median

            idx_pivot = self.__median_of_medians(left, self.idx_median)
            self.idx_median = self.__partition3(left, self.idx_median, idx_pivot)

            left_array = self.array[:self.idx_median]
            self.sum_left = sum(left_array)
            right_array = self.array[self.idx_median + 1:]
            self.sum_right = sum(right_array)
            # self.sum_right = self.sum_right + sum(self.array[self.idx_median + 1:idx_prev_median])
            # self.sum_left = self.sum_array - self.sum_right + self.array[self.idx_median]

            return self.__lwm_loop(left, self.idx_median)

        else:
            idx_prev_median = self.idx_median
            idx_pivot = self.__median_of_medians(self.idx_median, right)
            self.idx_median = self.__partition3(self.idx_median, right, idx_pivot)

            left_array = self.array[:self.idx_median]
            self.sum_left = sum(left_array)
            right_array = self.array[self.idx_median + 1:]
            self.sum_right = sum(right_array)
            # self.sum_left = self.sum_left + sum(self.array[idx_prev_median:self.idx_median - 1])
            # self.sum_right = self.sum_array + self.sum_left + self.array[self.idx_median]

            return self.__lwm_loop(self.idx_median, right)

    def select_median(self):
        pass

    def __median_of_medians(self, left, right):

        # for 5 or less elements just get median
        if right - left < 5:
            return self.__median_of_5(left, right)

        # otherwise move the medians of five - element subgroups to the first n / 5 positions
        idx = left
        while idx < right:
            # get the median position of the i 'th five-element subgroup
            sub_right = idx + 4
            if sub_right > right:
                sub_right = right
            median_of_5 = self.__median_of_5(idx, sub_right)

            saving_idx = left + math.floor((idx - left) / 5)
            self.__swap(median_of_5, saving_idx)
            idx += 5

        right = left + math.floor((right - left) / 5)
        return self.__median_of_medians(left, right)
