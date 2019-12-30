from core.util.debug import debug_lwm


class LowMedianWeighted(object):

    def __init__(self):
        self.array = []
        self.sum_array = None

        self.idx_median = None

    @property
    def result(self):
        if self.idx_median:
            return self.array[self.idx_median]
        else:
            return 0

    def lwm(self, array):

        self.array = array
        self.sum_array = self.__sum(array)

        # case of array full of 0
        if self.sum_array is 0:
            return 0

        check_value = self.sum_array / 2
        self.idx_median = self.__lwm_calculate(0, len(array) - 1, check_value)

    def __lwm_calculate(self, left, right, sumTarget):  # check_value

        med = (right - left) // 2
        sommaTotale = self.sum_array

        index = self.__select(left, right, med)
        debug_lwm(index)
        array_idx = self.__duplicated_values(index)
        sumLeftPivot = self.__sum(self.array[0:array_idx[0]])
        sumRightPivot = self.__sum(self.array[array_idx[1]:right+1])

        debug_lwm((sumLeftPivot, sumLeftPivot))
        while not (sumLeftPivot < sumTarget and sumRightPivot <= sumTarget):
            if sumLeftPivot >= sumTarget:
                tmpRight = index
                med = left + (tmpRight - left) / 2
                index = self.__select(left, tmpRight, med)

                array_idx = self.__duplicated_values(index)

                sumRightPivot = sumRightPivot + self.__sum(self.array[array_idx[1] + 1:tmpRight])
                sumLeftPivot = sommaTotale - sumRightPivot - self.__sum(self.array[array_idx[0]: array_idx[1]])

            else:
                tmpLeft = index
                med = tmpLeft + (right - tmpLeft) / 2
                index = self.__select(tmpLeft, right, med)

                array_idx = self.__duplicated_values(index)

                sumLeftPivot = sumLeftPivot + self.__sum(self.array[tmpLeft: array_idx[0] - 1])
                sumRightPivot = sommaTotale - sumLeftPivot - self.__sum(self.array[array_idx[0]:array_idx[1]])

            return index

    def __select(self, left, right, num):
        """
        :param left: lower index of the array.
        :param right: higher index of the array.
        """
        if right is left:
            return left

        # Find the median of medians
        median_of_medians = self.__median_of_medians(left, right)

        # Partition the array around the median of medians
        key = self.__partition(left, right, median_of_medians)
        
        """ 
        If key is the desired value return key
        else recursively select in relative subarray
        """

        if key[0] is num:
            return key[0]
        elif key[0] > num:
            return self.__select(left, key[0] - 1, num)
        elif key[0] < num:
            return self.__select(key[1], right, num)

    def __median_of_medians(self, left, right):
        """
        :param left: lower index of the array.
        :param right: higher index of the array.
        """
        # If the array is less then 5 elements, just get median
        dim = right - left
        if right - left <= 5:
            return self.__median_of_5(left, right)

        """
        1.  
        Divide the array in n/5 subarray of 5 elements each
        """
        start = left
        stop = left + 5
        medianPos = left
        iterations = dim//5

        idx = 0
        while idx < iterations:
            """
            2. 
            Find the median of each subarray picking the middle elements of the sorted subarray
            then move the medians of five value to the first n / 5 positions
            """
            median_of_5 = self.__median_of_5(start, stop-1)
            self.__swap(median_of_5, medianPos)
            medianPos += 1
            start = stop
            stop += 5
            idx += 1

        if start < dim:
            median_of_5 = self.__median_of_5(start, dim)
            self.__swap(median_of_5, medianPos)
            medianPos += 1
        """
        3.
        Do it recursively to find the median of medians
        """
        mid = left + (medianPos - left)//2
        return self.__select(left, medianPos, mid)

    def __partition(self, left, right, idx_pivot):

        pivot_el = self.array[idx_pivot]
        self.__swap(right, idx_pivot)

        low = left
        high = right - 1
        mid = left

        while mid <= high:
            if self.array[mid] < pivot_el:
                self.__swap(mid, low)
                mid += 1
                low += 1

            elif self.array[mid] > pivot_el:
                self.__swap(mid, high)
                high -= 1
            else:
                mid += 1

        high += 1
        self.__swap(right, high)
        return low, high

    def __median_of_5(self, left, right):
        self.__insertion_sort(left, right)
        median = (left+right) // 2
        debug_lwm('md5[{}:{}] {} median: {}'.format(left, right, self.array[left:right + 1], self.array[median]))
        return median

    def __insertion_sort(self, left, right):

        for idx in range(left+1, right+1):
            key = self.array[idx]

            # Move the elements of the array [0..idx-1],that are grater of the key to a right position.
            j = idx - 1
            while j >= left and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key

    def __duplicated_values(self, idx):

        x = idx

        while self.array[x] == self.array[x+1]:
            debug_lwm("{}\t{}".format(self.array[x], self.array[x + 1]))
            x += 1
        return idx, x

    def __swap(self, idx_1, idx_2):
        self.array[idx_1], self.array[idx_2] = self.array[idx_2], self.array[idx_1]

    @staticmethod
    def __sum(array):
        if not isinstance(array, list):
            return array
        result = 0
        for el in array:
            result += el
        return result
