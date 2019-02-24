"""
1) Recursive function
2) Built-in functions: min, max, count , len, split, zip,types, sum, sorted

"""

"""def prime_recursive(start, limit):

    if start == limit:
        return
    flag = True
    for divider in range(2, start):
        if start % divider == 0:
            flag = False
            break
    if flag:
        print(F'{start}is prime.')
    prime_recursive(start + 1, limit)


prime_recursive(2, 15)

"""
_list = [1, 3, 5, 24, 6, 7, 4, 2, 1, 3, 5, 7, 45]
print("Minimum List", min(_list))
print("Maximum List", max(_list))
print("Total elements in Lists are", _list.count(1))
#print(list.count([_list[0]]))
print("This is what you want to split".split(" "))
print("Lenth of list", len(_list))

fields = ['name', 'number']
values = ['Nilam', '9657236594']

for field, value in zip(fields, values):
    print(field, value)

_list1 = [1, "a", ['test'], {'test3': 'test4'}]

for i in _list:
    print(type(i), i)

print(sum(_list))
print(_list1)
_list.sort()
print(_list)
