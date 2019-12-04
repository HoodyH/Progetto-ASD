from core.util.base import Base


class Sorting(Base):

    def __init__(self):
        super().__init__()

    def insertion_sort(self):

        left = 0
        right = len(self.array) - 1

        for idx in range(left+1, right+1):

            key = self.array[idx]
            j = idx - 1
            while j >= left and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
