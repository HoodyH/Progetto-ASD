def read_input():

    try:
        data = input().replace(" ", "")  # take the input and remove the extra spaces
        input_array = data.split(",")  # split the sub substring
        input_array[-1] = input_array[-1][:-1]

        array = []
        for el in input_array:
            array.append(float(el))  # convert the element of the array to int

        return array

    except Exception as e:
        print(e)
        print('ERROR: bad input')
        return []
