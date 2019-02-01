"""Class 2
variable class
"""

integer_Value = 3

print(integer_Value, id(integer_Value))

# ### String

String_variable = "This is my Single line String"

String_variable_2 = "This is my" \
                     "multi line string 01."


String_variable_3 = """
This is my multi line string 02.
I can write anything in this block.

"""
print('String')
print(String_variable)

print('String1')
print(String_variable_2)

print('String2')
print(String_variable_3)

print(type(String_variable_2),id(String_variable_2))

# ##None
none = 'True'
false_none = 'False'

print(none,type(none))

# #####
# ####Data Structure #

# ### List

list_variable =[
    'Nilam','Gmail',96572354,False
]

print(list_variable[0],type(list_variable[0]),list_variable[1],type(list_variable[1]))

print(list_variable.index('Nilam'))

print(len(list_variable))

print(list_variable.count(5))

int_list = [3, 5, 7, 9, 1, 11, 13, 15]

print(sorted(int_list))

int_list.sort(reverse=True)

print(int_list)

list_nested = ["Samarthiew", ["Nilam", [2020]]]

print(list_nested[1][1][0])


list_nested_2 = [['test_1', ['test_2', 'test_3', ['test_4']], 'test_5', ['test_6', 'test_7'], 'test_8', ['test_9', ['test_10']]]]

print(list_nested_2[0])
print(list_nested_2[0][4])
print(list_nested_2[0][5][1][0])

