from core.util.sum import sum_array


class LowMedianWeightedInsertion:

    def __init__(self):
        self.array = []
        self.__result = None

    def lwm(self, array):
        self.array = array

        self.__insertion_sort()

        # calcolo il valore di controllo
        sum_tot = sum_array(self.array)/2

        _sum = 0

        """
        creo 2 variabili in cui andranno sommate i valori man mano che l'array viene controllato
        """
        for el in self.array:
            _sum += el

            """
            Ogni ciclo sommo il numero corrente
            a questo punto eseguo il controllo se sum_tot
            e' contenuto tra la sommatora senza l'elemento corrente e quella con'elemento corrente
            """
            if _sum-el < sum_tot <= _sum:
                self.__result = el
                return

    def __insertion_sort(self):
        left = 0
        right = len(self.array) - 1

        for idx in range(left+1, right+1):

            key = self.array[idx]
            """
            Sposta gli elementi di arr [0..i-1], che sono maggiori della chiave, 
            in una posizione avanti rispetto la loro posizione attuale
            """
            j = idx - 1
            while j >= left and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key

    @property
    def result(self):
        return self.__result
