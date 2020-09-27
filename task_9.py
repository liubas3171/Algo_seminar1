def find_common_elements(first_array, second_array):
    '''
    :param first_array: sorted list of ints with length N
    :param second_array: sorted list of ints with length N
    :return: None, prints elements that are in both arrays
    '''
    pointer = 0
    second_pointer = 0
    while pointer < len(first_array) and second_pointer < len(second_array):
        if first_array[pointer] == second_array[second_pointer]:
            print(first_array[pointer])
            pointer += 1
            second_pointer += 1
        elif first_array[pointer] < second_array[second_pointer]:
            pointer += 1
        else:
            second_pointer += 1


if __name__ == '__main__':
    a = [2, 3, 6, 9, 10, 11, 12]
    b = [2, 4, 6, 7, 8, 11, 13]
    find_common_elements(a, b)
