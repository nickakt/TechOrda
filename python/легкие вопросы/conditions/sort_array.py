list_to_sort = [40,3, 2, 1,15, 19]



def get_sorted_list(list_to_sort):
    for i in range(len(list_to_sort)):
        for j in range(0, len(list_to_sort) - i - 1):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
    return list_to_sort


print(get_sorted_list(list_to_sort))