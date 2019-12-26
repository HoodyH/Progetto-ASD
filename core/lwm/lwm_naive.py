class LowMedianWeightedNaive:

    def __init__(self):
        self.array = []
        self.__result = None

    def lwm(self, array):
        self.array = array
        self.__insertion_sort()

        sum_tot = sum(self.array)/2
        wk = 0
        sum1 = 0
        sum2 = 0  # self.array[0]

        for idx, el in enumerate(self.array):
            sum1 += wk  # sum the previous element respect the pivot
            sum2 += el
            wk = el

            if sum1 < sum_tot <= sum2:
                self.__result = wk

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

    @property
    def result(self):
        return self.result

