from random import randrange


class Sorting(object):

    @staticmethod
    def __partition(array, p, r):
        x = array[r]
        i = p - 1
        for idx in range(p, r-1):
            if array[idx] <= x:
                i = i+1
                array[i], array[idx] = array[idx], array[i]
        array[i+1], array[r] = array[r], array[i+1]
        return i+1

    def __rand_partition(self, array, p, r):
        i = randrange(p, r)
        array[i], array[r] = array[r], array[i]
        return self.__partition(array, p, r)

    def rand_select(self, array, p, r, i):
        if p is r:
            return array[p]
        q = self.__rand_partition(array, p, r)
        k = q - p + 1
        if i is k:
            return array[q]
        elif i < k:
            return self.rand_select(array, p, q-1, i)
        else:
            return self.rand_select(array, q + 1, r, i - k)