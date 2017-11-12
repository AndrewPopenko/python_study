def int_to_str(ist_num):
    list_str = []
    for item in ist_num:
        list_str.append(str(item))

    return list_str


def int_to_str_with_map(int_num):
    return list(map(str, int_num))


list_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_int_range = list(range(1, 11))

print(int_to_str(list_int))
print(int_to_str_with_map(range(1,11)))
print(list_int_range)