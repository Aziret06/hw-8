
def bubble_sort(some_list: list):
    for i in range(len(some_list) - 1):
        for num in range(len(some_list) - 1):
            if some_list[num] > some_list[num + 1]:
                some_list[num], some_list[num + 1] = some_list[num + 1], some_list[num]
        print(some_list)


bubble_sort([81, 14, 53, 1])
