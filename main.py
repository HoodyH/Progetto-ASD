from sorting.sorting import MedianOfMedians


def read_input():
    try:
        data = input()
        array =
        return array
    except Exception as e:
        print(e)
        return []


def main():
    array = [0.05, 0.05, 0.1, 0.1, 0.15, 0.2, 0.35]

    """
    s = Sorting()
    out = s.rand_select(array, 0, len(array)-1, 3)
    print(out)
    """

    m = MedianOfMedians(array)
    out = m.lower_weighted_median(0, len(array)-1)
    print(out)


if __name__ == "__main__":
    main()
