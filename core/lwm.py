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

        self.median_index = None

    @property
    def lwm(self):
        return self.array[self.median_index]

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

        pivot_idx = self.__pivot(left, right)
        self.median_index = self.__partition(left, right, pivot_idx)

        self.sum_left = sum(self.array[:self.median_index-1])
        self.sum_right = sum(self.array[self.median_index+1:])

        if self.sum_array is 0:
            return 0
        else:
            return self.__lwm_loop(left, right)

    def __lwm_loop(self, left, right):

        h_sum = self.sum_array / 2

        while True:

            print('S_left: {} < value: {} <= S_right: {}'.format(
                self.sum_left,
                self.array[self.median_index],
                self.sum_right)
            )

            if self.sum_left < h_sum <= self.sum_right:
                return self.array[self.median_index]

            elif self.sum_left >= h_sum:
                prev_media_index = self.median_index
                pivot_idx = self.__pivot(left, self.median_index)
                self.median_index = self.__partition(left, self.median_index, pivot_idx)

                self.sum_right = self.sum_right + sum(self.array[self.median_index+1:prev_media_index])
                self.sum_left = self.sum_array - self.sum_right + self.array[self.median_index]

                return self.__lwm_loop(left, self.median_index)

            else:
                prev_media_index = self.median_index
                pivot_idx = self.__pivot(self.median_index, right)
                self.median_index = self.__partition(self.median_index, right, pivot_idx)

                self.sum_left = self.sum_left + + sum(self.array[prev_media_index:self.median_index-1])
                self.sum_right = self.sum_array + self.sum_left + self.array[self.median_index]

                return self.__lwm_loop(self.median_index, right)

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
            self.array[median_of_5], self.array[saving_idx] = self.array[saving_idx], self.array[median_of_5]
            idx += 5

        right = left + math.floor((right - left) / 5)
        return self.__pivot(left, right)

    def __partition(self, left, right, pivot_idx):
        pivot_val = self.array[pivot_idx]

        # move pivot to the end
        self.array[pivot_idx], self.array[right] = self.array[right], self.array[pivot_idx]
        store_idx = left

        # move elements smaller then the pivot to the left
        for idx in range(left, right - 1):
            if self.array[idx] < pivot_val:
                self.array[store_idx], self.array[idx] = self.array[idx], self.array[store_idx]
                store_idx += 1

        store_idx_eq = store_idx
        for idx in range(store_idx, right - 1):
            if self.array[idx] == pivot_val:
                self.array[store_idx_eq], self.array[idx] = self.array[idx], self.array[store_idx_eq]
                store_idx_eq += 1

        # muove il pivot nella sua posizione finale
        self.array[store_idx_eq], self.array[right] = self.array[right], self.array[store_idx_eq]

        return store_idx_eq

    def __median_of_5(self, left, right):
        self.__insertion_sort(right, left)
        median = math.floor((left+right) / 2)
        print('median of 5 [{}:{}]: {} = {}'.format(left, right, self.array[left:right + 1], self.array[median]))
        return median

    def __insertion_sort(self, left, right):
        # parto ad ordinare dal vettore dal'indice 1 non da 0
        for idx in range(left + 1, right):
            key = self.array[idx]
            idx_check = idx - 1
            while idx_check >= left and self.array[idx_check] > key:
                self.array[idx_check + 1] = self.array[idx_check]
                idx_check -= 1

            self.array[idx_check + 1] = key


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
