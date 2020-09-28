def elem_in_array(element, array):
    '''
    :param element: int
    :param array: sorted list of ints
    :return: True if element is in array, False otherwise
    '''

    length = len(array)
    fib_num_2_back = 0
    fib_num_1_back = 1
    fib_num = fib_num_2_back + fib_num_1_back

    while (fib_num < length):
        fib_num_2_back = fib_num_1_back
        fib_num_1_back = fib_num
        fib_num = fib_num_2_back + fib_num_1_back

    floor_pointer = -1

    while (fib_num > 1):
        index = min(floor_pointer + fib_num_2_back, length - 1)

        if (array[index] < element):
            fib_num = fib_num_1_back
            fib_num_1_back = fib_num_2_back
            fib_num_2_back = fib_num - fib_num_1_back
            floor_pointer = index

        elif (array[index] > element):
            fib_num = fib_num_2_back
            fib_num_1_back = fib_num_1_back - fib_num_2_back
            fib_num_2_back = fib_num - fib_num_1_back

        else:
            return True

    if (fib_num_1_back and floor_pointer + 1 < len(array) - 1) and \
            (array[floor_pointer + 1] == element):
        return True

    return False


if __name__ == "__main__":
    array = [2, 5, 8, 14, 22, 33, 48, 59, 60, 62]
    el = 5
    print(elem_in_array(el, array))
