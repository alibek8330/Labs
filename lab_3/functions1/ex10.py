def unique_elements(string):
    list = [int(x) for x in string.split()]
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

string = input()
print(unique_elements(string))

