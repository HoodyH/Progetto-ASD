
def median_of_medians(array, i):

    # divide A into sublists of len 5
    lists_of_five = [list[j:j + 5] for j in range(0, len(array), 5)]
    medians = [sorted(list_of_five)[int(len(list_of_five) / 2)] for list_of_five in lists_of_five]
    if len(medians) <= 5:
        pivot = sorted(medians)[int(len(medians) / 2)]
    else:
        # il pivot è la mediana delle mediane
        pivot = median_of_medians(medians, len(medians) / 2)

    # partitioning step
    low = [j for j in array if j < pivot]
    high = [j for j in array if j > pivot]

    k = len(low)
    if i < k:
        return median_of_medians(low, i)
    elif i > k:
        return median_of_medians(high, i - k - 1)
    else:  # pivot = k
        return pivot
