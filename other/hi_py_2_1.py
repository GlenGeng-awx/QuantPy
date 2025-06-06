l1 = [i for i in range(1, 10)]
l2 = [i for i in reversed(range(1, 10))]

print(l1)
print(l2)
print(l1[:-2])

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)
print(dict1)

value = (1, 2, 3)
if type(value) is tuple:
    print("value is tuple")
