"""Implementing merge sort for a string"""

def merge_string(string: list, start: int, midpoint: int, end: int):
    """
    merge: does the merge operation in merge sort algorithm
    @param string: the list of characters to be merged after sorting
    @param start: the start index
    @param midpoint: the middle point index in the list
    @param end: the end index 
    """
    left_str_len = (midpoint - start) + 1
    right_str_len = end - midpoint

    left = [string[start + i] for i in range(left_str_len)]
    right = [string[midpoint + i + 1] for i in range(right_str_len)]

    i, j, k = 0, 0, start
    while i < left_str_len and j < right_str_len:
        if left[i] <= right[j]:
            string[k] = left[i]
            i += 1
        else:
            string[k] = right[j]
            j += 1
        k += 1
    
    while i < left_str_len:
        string[k] = left[i]
        k += 1
        i += 1
    
    while j < right_str_len:
        string[k] = right[j]
        k += 1
        j+= 1

def merge_sort_string(string: list, start: int, end: int) -> str:
    """
    merge_sort: sort a list of characters using merge sort algorithm
    @param string: the list of characters to be sorted
    @start: the index of the first element
    @end: the index of the last element

    Returns:
        a sorted string
    """
    if start >= end:
        return
    
    midpoint = (start + end) // 2
    merge_sort_string(string, start, midpoint)
    merge_sort_string(string, midpoint + 1, end)
    merge_string(string, start, midpoint, end)

    return "".join(string)

def merge_list(array: list, start: int, midpoint: int, end: int):
    """
    merge_sort_list: a function that merges a list of aorted elements by merge sort
    @param array: the list of elements to merge
    @param start: the index of the starting element
    @param midpoint: the index of the middle element
    @param end: the index of the last element
    """
    left_list_len = (midpoint - start) + 1
    right_list_len = end - midpoint

    left = [array[start + i] for i in range(left_list_len)]
    right = [array[midpoint + i + 1] for i in range(right_list_len)]

    i, j, k = 0, 0, start
    while i < left_list_len and j < right_list_len:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    
    while i < left_list_len:
        array[k] = left[i]
        k += 1
        i += 1
    
    while j < right_list_len:
        array[k] = right[j]
        k += 1
        j += 1

def merge_sort_list(array: list, start: int, end: int):
    """
    merge_sort_list: a function to sort a list of strings
    @param array: the list of items
    @param start: the index of the starting element
    @param end: the index of the last element
    """
    if start >= end:
        return
    
    midpoint = (start + end) // 2
    merge_sort_list(array, start, midpoint)
    merge_sort_list(array, midpoint + 1, end)
    merge_list(array, start, midpoint, end)

def main():
    array_words = ['cat', 'sleep', 'laugh', 'a', 'abbracadabra', 'sorting', 'python', 'acme']
    # print array before sorting
    for item in array_words:
        print(item, end=' ')
    print()

    for i in range(len(array_words)):
        if len(array_words[i]) <= 1:
            continue
        # sort the strings individually
        array_words[i] = merge_sort_string(list(array_words[i]), 0, len(array_words[i]) - 1)
    # sort the entire array and the strings in it
    merge_sort_list(array_words, 0, len(array_words) - 1)

    # print array after sorting
    for item in array_words:
        print(item, end=' ')
    print()

if __name__ == '__main__':
    main()