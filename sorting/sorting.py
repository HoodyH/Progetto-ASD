import math


class MedianOfMedians(object):

    def __init__(self, array):
        """
        :param array: vettore contenente i dati
        """

        self.array = []
        self.array_sum = None
        """
        Per salvare la somma ad ogni ciclo
        evitando di ricalcolare completamente.
        """
        self.sum_left = None
        self.sum_right = None

    def calculate_lwm(self, array, left, right):
        """
        Metodo che esegue il calcolo
        :param array:
        :param left:
        :param right:
        :return:
        """
        self.array = array
        self.array_sum = sum(array)

        self.sum_left = 1
        self.sum_right = 1

        return self.lwm_loop(left, right)

    def lwm_loop(self, left, right):

        while True:
            if left is right:
                return left
            pivot_idx = self.pivot(left, right)

            median_index = self.partition(left, right, pivot_idx)

            sum_left = sum(self.array[:median_index-1])
            sum_right = sum(self.array[median_index+1:right-1])

            if sum_left < self.array_sum/2 and sum_right <= self.array_sum/2:
                return self.array[median_index]
            elif sum_left >= self.array_sum/2:
                return self.lwm_loop(0, median_index + 1)
            else:
                return self.lwm_loop(median_index - 1, len(self.array)-1)

    def pivot(self, left, right):

        # for 5 or less elements just get median
        if right - left < 5:
            return self.median_of_5(left, right)

        # otherwise move the medians of five - element subgroups to the first n / 5 positions
        idx = 0
        while idx < right:
            # get the median position of the i 'th five-element subgroup
            sub_right = idx + 4
            if sub_right > right:
                sub_right = right
            median_of_5 = self.median_of_5(idx, sub_right)

            saving_idx = left + math.floor((idx - left) / 5)
            self.array[median_of_5], self.array[saving_idx] = self.array[saving_idx], self.array[median_of_5]
            idx += 5

        right = left + math.floor((right - left) / 5)
        return self.pivot(left, right)

    def partition(self, left, right, pivot_idx):
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

    def median_of_5(self, left, right):
        self.insertion_sort(right, left)
        print('median of 5 [{}:{}]: {}'.format(left, right, self.array[left:right+1]))
        median = math.floor((left+right) / 2)
        print('median: {}'.format(self.array[median]))
        return median

    def insertion_sort(self, left, right):
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
