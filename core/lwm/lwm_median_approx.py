from core.util.debug import debug_lwm
from core.util.sum import sum_array


class LowMedianWeightedMedianApprox(object):

    def __init__(self):
        self.array = []
        self.sum_array = None

        self.idx_median = None  # result

    @property
    def result(self):
        if self.idx_median:
            return self.array[self.idx_median]
        else:
            return 0

    def lwm(self, array):

        self.array = array
        self.sum_array = sum_array(array)

        # case of array full of 0
        if self.sum_array is 0:
            return 0

        check_value = self.sum_array / 2
        self.idx_median = self.__select(0, len(array) - 1, check_value)

    def __select(self, left, right, check_value):
        """
        :param left: lower index of the array.
        :param right: higher index of the array.
        :param check_value: the control value
        """

        x = self.__median_of_medians(left, right)

        """
        4. 
        Partition the array around the median of medians
        """
        key = self.__partition(left, right, x)

        # Add all the elements smaller or equal than the key (excluded)
        partial_sum = sum_array(self.array[left:key])

        """
        5.
        If adding the key to the partial_sum
        makes this greater than the target return the key,
        else recursively select in relative subarray
        """
        debug_lwm('median: {}'.format(self.array[key]))

        if check_value > partial_sum >= check_value - self.array[key]:
            return key
        elif partial_sum == check_value:
            return key - 1
        elif partial_sum > check_value:
            return self.__select(left, key, check_value)
        else:
            return self.__select(key, right, check_value - partial_sum)

    def __median_of_medians(self, left, right):
        """
        :param left: lower index of the array.
        :param right: higher index of the array.
        """
        if right is left:
            return left

        # If the array is less then 5 elements, just get median
        if right - left < 5:
            return self.__median_of_5(left, right)

        """
        1.  
        Divide the array in n/5 subarray of 5 elements each
        """
        idx = left
        while idx < right:
            # get the median position of the i 'th five-element subgroup
            sub_right = idx + 4
            if sub_right > right:
                sub_right = right
            """
            2. 
            Find the median of each subarray picking the middle elements of the sorted subarray
            then move the medians of five value to the first n / 5 positions
            """
            median_of_5 = self.__median_of_5(idx, sub_right)
            saving_idx = left + (idx - left) // 5
            self.__swap(median_of_5, saving_idx)

            idx += 5

        right = left + (right - left) // 5
        """
        3.
        Do it recursively to find the median of medians
        """
        return self.__median_of_medians(left, right)

    def __partition(self, left, right, idx_pivot):
        mid = low = left
        high = right
        pivot_el = self.array[idx_pivot]

        while mid <= high:
            if self.array[mid] < pivot_el:
                self.__swap(low, mid)
                low += 1
                mid += 1

            elif self.array[mid] > pivot_el:
                self.__swap(mid, high)
                high -= 1
            elif self.array[mid] == pivot_el:
                mid += 1

        if low is high:
            return low
        else:
            return (low+high) // 2

    def __median_of_5(self, left, right):
        self.__insertion_sort(left, right)
        median = (left+right) // 2
        debug_lwm('md5[{}:{}] {} median: {}'.format(left, right, self.array[left:right], self.array[median]))
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

    def __swap(self, idx_1, idx_2):
        self.array[idx_1], self.array[idx_2] = self.array[idx_2], self.array[idx_1]
