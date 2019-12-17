class LowMedianWeighted(object):

    def __init__(self):
        self.array = []
        self.sum_array = None
        """
        Per salvare la somma ad ogni ciclo
        evitando di ricalcolare completamente.
        """

        self.idx_median = None

    @property
    def result(self):
        if self.idx_median:
            return self.array[self.idx_median]
        else:
            return 0

    def lwm(self, array, left, right):

        self.array = array
        self.sum_array = sum(array)

        # case of array full of 0
        if self.sum_array is 0:
            return 0

        check_value = self.sum_array / 2
        self.idx_median = self.__lwm_calculate(left, right, check_value)

    def __lwm_calculate(self, left, right, check_value):

        # Find the values who will work as key
        key = self.__select(left, right)
        idx_lwm = self.__partition(left, right, key)

        # Add all the elements smaller or equal than the key (excluded)
        partial_sum = sum(self.array[left:idx_lwm])

        """
        If adding the key to the partial_sum
        makes this greater than the target return the key,
        else recursively search in the relative subarray
        """
        if check_value > partial_sum >= check_value - self.array[idx_lwm]:
            return idx_lwm
        elif partial_sum == check_value:
            return idx_lwm - 1
        elif partial_sum > check_value:
            return self.__lwm_calculate(left, idx_lwm, check_value)
        else:
            return self.__lwm_calculate(idx_lwm, right, check_value - partial_sum)

    def __select(self, left, right):
        """
        :param left: lower index of the array.
        :param right: higher index of the array.
        """

        # Find the median of medians
        median_of_medians = self.__median_of_medians(left, right)

        # Partition the array around the median of medians
        key = self.__partition(left, right, median_of_medians)
        
        """ 
        If key is the desired value return key
        else recursively select in relative subarray
        """
        mid1e_idx = (right + left) // 2

        if key == mid1e_idx:
            return key
        elif key > mid1e_idx:
            return self.__select(left, key - 1)
        elif key < mid1e_idx:
            return self.__select(key, right)

    def __median_of_medians(self, left, right):
        """
        :param left: lower index of the array.
        :param right: higher index of the array.
        """
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
        j = i = left
        dim = right
        pivot_el = self.array[idx_pivot]

        while j <= dim:
            if self.array[j] < pivot_el:
                self.__swap(i, j)
                i += 1
                j += 1

            elif self.array[j] > pivot_el:
                self.__swap(j, dim)
                dim -= 1
            else:
                j += 1

        if i is dim:
            return i
        else:
            return (i+dim) // 2

    def __median_of_5(self, left, right):
        self.__insertion_sort(left, right)
        median = (left+right) // 2
        print('median5 [{}:{}]: {} = {}'.format(left, right, self.array[left:right + 1], self.array[median]))
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
