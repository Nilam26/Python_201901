"""
Data Structure : Dictionary , Tuple ,set
"""

dictionary_variable = {'name': 'Nilam', 'Address': 'Pune', 'mobile no': 9657236594}


print(dictionary_variable)

print(dictionary_variable['name'])
print(dictionary_variable['Address'])

print(dictionary_variable.get('mobile no', "Key does not found"))
print(dictionary_variable.get('Cont_no', "Key does not found"))

print(dictionary_variable.keys())  # ## get keys of dictionary
print(dictionary_variable.values())
print(dictionary_variable.items())

print(dictionary_variable)

Cont_no = dictionary_variable['mobile no']
dictionary_variable.pop('mobile no')

print(dictionary_variable)

dictionary_variable['Cont_no'] = Cont_no
print(dictionary_variable)

dict_01 = [{'test1': 'test2', 'test3': 'test4'},
       {'test5': [
              {'test6': 'test7', 'test8': 'test9'},
              {'test10': 'test11', 'test12': 'test13'}
    ]
}
]
print(dict_01[1]['test5'][1]['test12'])
# ##a = dict_01[1]
# ##print(a)
# ##b = a['test5']
# ##print(b[1])
# ##print(b['test12'])


dict_02 = {
    'test1': 'test2', 'test3': [
        {'test4': 'test5', 'test6': ['test7', 'test8']},
        [{'test9': 'test10'}, 'test11',
         {'test12': 'test13', 'test14': 'print_me'}
         ],
        {'test15': 'print_me2'}
    ]
}
print(dict_02['test3'][1][2]['test14'])
print(dict_02['test3'][2]['test15'])


tuple_variable = (1, )
print(tuple_variable[1])

x = [1, 1, 2, 2, 3, 4, 5, 5, 8]

print(set[x])
