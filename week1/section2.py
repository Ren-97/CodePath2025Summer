def delete_minimum_elements(hunny_jar_sizes):
    new_list = []
    while hunny_jar_sizes:
        element = min(hunny_jar_sizes)
        new_list.append(element)
        hunny_jar_sizes.remove(element)
    return new_list

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))