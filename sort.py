
def bubble_sort(some_list: list):
    for i in range(len(some_list) - 1):
        for num in range(len(some_list) - 1):
            if some_list[num] > some_list[num + 1]:
                some_list[num], some_list[num + 1] = some_list[num + 1], some_list[num]
        print(some_list)


bubble_sort([81, 14, 53, 1, 17, 28, 0])


def binary_search(search_element, list_to_search: list):
    pos = 0
    result_ok = False
    first = 0
    last = len(list_to_search) - 1

    while first <= last:
        middle = (first + last) // 2
        if search_element == list_to_search[middle]:
            first = middle
            last = first - 1
            result_ok = True
            pos = middle
        elif search_element > list_to_search[middle]:
            first = middle + 1
        else:
            last = middle - 1
    if result_ok:
        print(f'The element is found, position: {pos}')
    else:
        print(f'The element is not found')


binary_search(42, [1, 12, 14, 18, 16, 21, 22, 28, 32, 33, 37, 39, 40, 42, 45, 48, 50])
