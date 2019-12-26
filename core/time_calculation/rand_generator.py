from time import time
from core.time_calculation.seed_storage import SeedStorage


class RandGenerator(object):

    def __init__(self):
        self.seeds = SeedStorage()
        self.seeds.insert(time())

    def __pseudo_random(self):
        seed = self.seeds.get_seed()
        a = 16807
        m = 2147483647
        q = 127773
        r = 2836
        hi = int(seed / q)
        lo = seed - q * hi
        test = a * lo - r * hi
        if test < 0:
            self.seeds.delete()
            self.seeds.insert(test + m)
        else:
            self.seeds.delete()
            self.seeds.insert(test)

        return seed / m

    def generate_array(self, num_elements):

        random_array = []
        for i in range(num_elements):
            random_array.append(self.__pseudo_random())

        return random_array
