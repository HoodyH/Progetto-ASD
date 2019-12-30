from core.util.sum import sum_array


class LowMedianWeightedMerge:

    def __init__(self):
        self.array = []
        self.__result = None

    def lwm(self, array):
        """
        :param array: l'array nel quale trovare la mediana pesata inferiore
        :return:
        """
        self.array = array

        self.__merge_sort(self.array)

        # calcolo il valore di controllo
        sum_tot = sum_array(self.array) / 2

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
            if _sum - el < sum_tot <= _sum:
                self.__result = el
                return

    def __merge_sort(self, array):

        """
        :param array: l'array da ordinare
        """
        array_len = len(array)
        if array_len > 1:

            center = array_len // 2
            # array tem
            temp_left = array[:center]  # Dividing the array elements
            temp_right = array[center:]  # into 2 halves

            self.__merge_sort(temp_left)
            self.__merge_sort(temp_right)

            i = j = k = 0
            """
            Unisce due subarrays di arr [].
            Il primo subarray è arr [l..m]
            Il secondo subarray è arr [m + 1..r]
            
            Copia i dati da temp array temp_left[] and temp_right[] nell'array di origine
            """
            while i < len(temp_left) and j < len(temp_right):
                if temp_left[i] < temp_right[j]:
                    array[k] = temp_left[i]
                    i += 1
                else:
                    array[k] = temp_right[j]
                    j += 1
                k += 1

            # Controlla se ci sono elementi rimasti a sinistra
            while i < len(temp_left):
                array[k] = temp_left[i]
                i += 1
                k += 1

            # Controlla se ci sono elementi rimasti a sinistra
            while j < len(temp_right):
                array[k] = temp_right[j]
                j += 1
                k += 1

    @property
    def result(self):
        return self.__result
