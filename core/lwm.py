import math


class MedianOfMedians(object):

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
    def lwm(self):
        return self.array[self.idx_median]

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

        idx_pivot = self.__pivot(left, right)
        self.idx_median = self.__partition3(left, right, idx_pivot)

        self.sum_left = sum(self.array[:self.idx_median - 1])
        self.sum_right = sum(self.array[self.idx_median + 1:])

        if self.sum_array is 0:
            return 0
        else:
            return self.__lwm_loop(left, right)

    def __lwm_loop(self, left, right):

        h_sum = self.sum_array / 2

        while True:

            print('S_left: {} < value: {} <= S_right: {}'.format(
                self.sum_left,
                self.array[self.idx_median],
                self.sum_right)
            )

            if self.sum_left < h_sum <= self.sum_right:
                return self.array[self.idx_median]

            elif self.sum_left >= h_sum:
                prev_media_index = self.idx_median
                idx_pivot = self.__pivot(left, self.idx_median)
                self.idx_median = self.__partition3(left, self.idx_median, idx_pivot)

                self.sum_right = self.sum_right + sum(self.array[self.idx_median + 1:prev_media_index])
                self.sum_left = self.sum_array - self.sum_right + self.array[self.idx_median]

                return self.__lwm_loop(left, self.idx_median)

            else:
                prev_media_index = self.idx_median
                idx_pivot = self.__pivot(self.idx_median, right)
                self.idx_median = self.__partition3(self.idx_median, right, idx_pivot)

                self.sum_left = self.sum_left + sum(self.array[prev_media_index:self.idx_median - 1])
                self.sum_right = self.sum_array + self.sum_left + self.array[self.idx_median]

                return self.__lwm_loop(self.idx_median, right)

    def __pivot(self, left, right):

        # for 5 or less elements just get median
        if right - left < 5:
            return self.__median_of_5(left, right)

        # otherwise move the medians of five - element subgroups to the first n / 5 positions
        idx = 0
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
        return self.__pivot(left, right)

    def __partition3(self, left, right, idx_pivot):
        j = i = left
        dim = right

        while j <= dim:
            if self.array[j] < self.array[idx_pivot]:
                self.__swap(i, j)
                i += 1
                j += 1

            elif self.array[j] > self.array[idx_pivot]:
                self.__swap(j, dim)
                dim -= 1
            else:
                j += 1

        return int((i+dim)/2)

    """
    def __partition(self, left, right, pivot_idx):
        pivot_val = self.array[pivot_idx]

        # move idx_pivot to the end
        self.__swap(pivot_idx, right)
        store_idx = left

        # move elements smaller then the idx_pivot to the left
        for idx in range(left, right - 1):
            if self.array[idx] < pivot_val:
                self.__swap(store_idx, idx)
                store_idx += 1

        store_idx_eq = store_idx
        for idx in range(store_idx, right - 1):
            if self.array[idx] == pivot_val:
                self.__swap(store_idx_eq, idx)
                store_idx_eq += 1

        # muove il idx_pivot nella sua posizione finale
        self.__swap(store_idx_eq, right)

        return store_idx_eq
    """

    def __median_of_5(self, left, right):
        self.__insertion_sort(left, right)
        median = math.floor((left+right) / 2)
        print('median5 [{}:{}]: {} = {}'.format(left, right, self.array[left:right + 1], self.array[median]))
        return median

    def __insertion_sort(self, left, right):

        for idx in range(left+1, right+1):

            key = self.array[idx]
            """
            Sposta gli elementi dell'array[0..idx-1], che sono maggiori della chiave
            ad una posizione avanti rispetto alla corrente
            """
            j = idx - 1
            while j >= left and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key

    def __swap(self, idx_1, idx_2):
        self.array[idx_1], self.array[idx_2] = self.array[idx_2], self.array[idx_1]


"""
    def partition5(self, left, right):
        i = left + 1
        while i <= right:
            j = i
            while j > left and self.array[j - 1] > self.array[j]:

                j -= 1
            i -= 1
        return math.floor((left + right) / 2)
"""
