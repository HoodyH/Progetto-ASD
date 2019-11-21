#!/usr/bin/env python
from sorting.sorting import MedianOfMedians


EXAMPLE_ARRAY = [0.05, 0.05, 0.1, 0.1, 0.15, 0.2, 0.35]


def read_input():
    try:
        data = input().replace(" ", "")  # take the input and remove the extra spaces
        array_of_char = data.split(",")  # split the sub substring

        array = []
        for el in array_of_char:
            end_dot = el.find('.', el.find('.')+1)
            if end_dot is not -1:
                array.append(float(el[:end_dot]))  # if there is the end point add the last element then break
                break
            array.append(float(el))  # convert the element of the array to int

        return array

    except Exception as e:
        print(e)
        print('ERROR: bad input')
        return []


def main():

    array = read_input()
    print(array)
    """
    s = Sorting()
    out = s.rand_select(array, 0, len(array)-1, 3)
    print(out)
    """
    return

    m = MedianOfMedians(array)
    out = m.lower_weighted_median(0, len(array)-1)
    print(out)


if __name__ == "__main__":
    main()
