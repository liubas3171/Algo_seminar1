def binary_search(element, array):
    '''
    :param element: int
    :param array: sorted list of ints
    :return: True if element is in array, False otherwise
    '''
    floor = 0
    ceil = len(array)
    while (ceil - floor) > 1:
        pointer = (ceil + floor) // 2
        if array[pointer] == element:
            return True
        elif array[pointer] < element:
            floor = pointer
        else:
            ceil = pointer
    return False


if __name__ == '__main__':
    vector = [2, 4, 6, 8, 12, 13, 15]
    print(binary_search(12, vector))
