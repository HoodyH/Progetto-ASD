class Seed:

    def __init__(self):
        self.__data = None
        self.__next_seed = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next_seed(self):
        return self.__next_seed

    @next_seed.setter
    def next_seed(self, value):
        self.__next_seed = value


class SeedStorage:

    def __init__(self):
        self.__current = None

    def get_seed(self):
        value = self.__current.data
        return value

    def insert(self, data):
        new_seed = Seed()
        new_seed.data = data
        new_seed.next = self.__current
        self.__current = new_seed

    def delete(self):
        temp = self.__current
        self.__current = self.__current.next_seed
        return temp
