class SeedGenerator(object):

    def __init__(self):
        self. seeds = []

    def pseudo_random(self):
        seed = self.seeds[-1]
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

    def generate_array(self, num_elements):

        random_array = []
        while range(num_elements):
            random_array.append(self.pseudo_random())
