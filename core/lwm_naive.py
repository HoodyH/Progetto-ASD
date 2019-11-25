

class LowMedianWeightedNaive(object):

    def __init__(self):
        self.array = []

    def lwm_calculate(self, array):
        self.array = array
        self.__insertion_sort()

        sum_weights = sum(self.array)
        wk = 0
        sum1 = 0
        sum2 = self.array[0]

        for idx, el in enumerate(self.array):
            wk = el
            sum1 += self.__get_element(idx, wk)
            sum2 += self.__get_element(idx + 1, wk, equal=True)

            if sum1 < sum_weights <= sum2:
                return wk

    def __insertion_sort(self):
        left = 0
        right = len(self.array) - 1

        for idx in range(left+1, right+1):

            key = self.array[idx]
            j = idx - 1
            while j >= left and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key

    def __get_element(self, index, value, equal=False):
        if equal:
            return self.array[index]
        else:
            while self.array[index] >= value:
                if index is 0:
                    return 0
                index -= 1
            return self.array[index]