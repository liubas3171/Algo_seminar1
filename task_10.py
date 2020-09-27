def merge(array1, array2):
    '''
    :param array1: sorted list
    :param array2: sorted list
    :return: list, merged from 2 arrays
    '''
    res = []
    pointer1 = 0
    pointer2 = 0
    while pointer1 < len(array1) and pointer2 < len(array2):
        if array1[pointer1] <= array2[pointer2]:
            res.append(array1[pointer1])
            pointer1 += 1
        else:
            res.append(array2[pointer2])
            pointer2 += 1
    res += array1[pointer1: len(array1)]
    res += array2[pointer2: len(array2)]
    return res


def merge_sort(array):
    '''

    :param array: array of numbers
    :return: list, sorted array of numbers
    '''
    if len(array) < 2:
        return array
    else:
        divider = len(array) // 2
        lst1 = merge_sort(array[:divider])
        lst2 = merge_sort(array[divider:])
        return merge(lst1, lst2)


def find_two_closest(array):
    '''
    :param array: list of numbers
    :return: list, two numbers with difference less than in any other 2 numbers in array.
    '''
    sorted_array = merge_sort(array)
    res = list()
    res.append(sorted_array[0])
    res.append(sorted_array[1])

    for i in range(1, len(sorted_array) - 1):
        if abs(res[0] - res[1]) > abs(sorted_array[i] - sorted_array[i + 1]):
            res[0] = sorted_array[i]
            res[1] = sorted_array[i + 1]
    return res


if __name__ == '__main__':
    a = [3, 10, 20, 2, 50, 5, 90, 100]
    print(find_two_closest(a))
    
    
# Calculating complexity:
# Sorting - O(nlog(n))
# Finding pair - O(n)
# General: O(n + nlog(n)) = O(nlog(n))
