class LowMedianWeightedNaive:

    def __init__(self):
        self.array = []
        self.__result = None

    def lwm(self, array):
        self.array = array

        # self.__insertion_sort()
        self.__merge_sort(self.array)

        sum_tot = sum(self.array)/2
        wk = 0
        sum1 = 0
        sum2 = 0

        for el in self.array:
            sum1 += wk  # sum the previous element
            sum2 += el
            wk = el

            if sum1 < sum_tot <= sum2:
                self.__result = wk
                return

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

    def __merge_sort(self, array):

        array_len = len(array)
        if array_len > 1:

            center = array_len // 2
            temp_left = array[:center]  # Dividing the array elements
            temp_right = array[center:]  # into 2 halves

            self.__merge_sort(temp_left)
            self.__merge_sort(temp_right)

            i = j = k = 0

            # Copy data to temp arrays temp_left[] and temp_right[]
            while i < len(temp_left) and j < len(temp_right):
                if temp_left[i] < temp_right[j]:
                    array[k] = temp_left[i]
                    i += 1
                else:
                    array[k] = temp_right[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(temp_left):
                array[k] = temp_left[i]
                i += 1
                k += 1

            while j < len(temp_right):
                array[k] = temp_right[j]
                j += 1
                k += 1

    @property
    def result(self):
        return self.__result
