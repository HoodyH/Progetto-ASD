

class LowMedianWeightedNaive(object):

    def lwm_calculate(self, array, left, right):
        sum_weights = sum(array)
        wk = 0
        sum1 = 0
        sum2 = array[0]

        for idx, el in enumerate(array):
            wk = el
            sum1 += self.__get_element(array, idx, wk)
            sum2 += self.__get_element(array, idx + 1, wk, equal=True)

            if sum1 < sum_weights <= sum2:
                return wk

    @staticmethod
    def __get_element(array, index, value, equal=False):
        if equal:
            return array[index]
        else:
            while array[index] >= value:
                if index is 0:
                    return 0
                index -= 1
            return array[index]