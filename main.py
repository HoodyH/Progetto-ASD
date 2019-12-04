#!/usr/bin/env python
from core.lwm_naive import LowMedianWeightedNaive
from core.lwm import LowMedianWeighted


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


def prod():

    array = read_input()
    print('Input' + str(array))

    m_naive = LowMedianWeightedNaive()
    out_naive = m_naive.lwm_calculate(array)

    m = LowMedianWeighted()
    # out = m.lwm_calculate(array, 0, len(array) - 1)

    print('lwm naive: {}'.format(out_naive))
    # print('lwm: {}'.format(out))


def test():

    # Here are some example lists you can use to see how the algorithm works
    a_list = [1, 2, 3, 4, 5, 1000, 8, 9, 99]
    b_list = [1, 2, 3, 4, 5, 6]
    print(median_of_medians(a_list, 0))  # should be 1
    print(median_of_medians(a_list, 7))  # should be 99
    print(median_of_medians(b_list, 4))  # should be 5


def main():
    prod()


if __name__ == '__main__':
    main()
