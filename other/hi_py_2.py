import copy

prev_list = [[1, 2, 3]]

list1 = copy.deepcopy(prev_list)
list2 = copy.deepcopy(prev_list)

list1.append(4)
list2.append(5)

print(prev_list)
print(list1)
print(list2)

