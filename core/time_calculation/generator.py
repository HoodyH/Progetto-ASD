class SeedGenerator(object):

    def __init__(self):
        self. seeds = []

    def generate_seed(self):
        seed = self.seeds.getSeed()
        a = 16807
        m = 2147483647
        q = 127773
        r = 2836
        hi = int(seed / q)
        lo = seed - q * hi
        test = a * lo - r * hi
        if test < 0:
            self.seeds.pop()
            self.seeds.append(test + m)
        else:
            self.seeds.pop()
            self.seeds.append(test)

        return seed / m