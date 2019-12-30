def sum_array(array):
    if not isinstance(array, list):
        return array
    result = 0
    for el in array:
        result += el
    return result
