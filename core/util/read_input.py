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
