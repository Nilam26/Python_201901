"""
1)Comprehension
2)User Defined Function

#Assignment
1)Write List comprehension to create 15 random no`s
2)Write List comprehension to create 15 prime no`s till user defined nos
3)Write Dictionary comprehension with 5 key value pair
4)Convert all pattern assignments in user defined Function

"""

# ##############
# Comprehension
# ########

# ##List Comprehension
"""
_odd = list()

for i in range(1,10,2):
    _odd.append(i)
print(_odd)

print("Comprehension")
_odd = [i for i in range(1,10,2)]
print(_odd)

print("second option")
for i in range(1,10):
    if i%2 == 1:
        _odd.append(i)
print(_odd)

print("Comprehension2")
_odd = [j for j in range(1,10) if j%2 == 1]
print(_odd)

### Dictionary comprehension

sqr = {}

numbers = [2, 4, 6, 7, 8, 9, 11]
for  num in numbers:
   sqr[num] = num  * num
print(sqr)

print("Disctionary comprehension")
_sq={num: num*num for num in numbers}
print(_sq)
"""
labels = ['Name', 'Age', 'Contact No']
user_1 = ['Nilam', 25 , 96572359]
user_2 = ['xyz', 35 , 88572359]
user_3 = ['abc',20, 88888888]

op = list()
for user in [user_1,user_2, user_3]:
    _user = dict()
    for index in range(0,3):
        _user[labels[index]]=user[index]
        op.append(_user)
print(op)

print("comprehension with index")
output = [
 {
 labels[index]: user[index] for index in range(0,3)
 for user in [user_1 , user_2, user_3]}
 ]
print(output)

# #######
# User Defined Functions
###########

'''
def<function_name>():
    """
    Function Doc string
    """ 
    <Statement 1>
    <statement 2>
    .
    .
    .
    <statement n>

'''

def greetings():
    """
    This is greeting function
    """
    print("hello world")
greetings()


def arg_greetings(name):
    """
    this is greeting function with argument
    :param name:l
    :return:
    """
    print("hello {}".format(name))
    print(F"Hello{name}")
arg_greetings(name="Nilam")

def arg_return_greetings(name):

    """
    This is greeting function with arguments and return greeting message

    :param name:
    :return:
    """
    message = F"hello {name}"
    return message
#name = input("Enter name:")
rep = arg_return_greetings("Nilam")
print(rep)


def wild_card_args_greetings(*args):
    """

    :param args:
    :return:
    """

    print(args[0], args[1])
wild_card_args_greetings(*['test','test1'])


def wild_card_kwargs_function(**kwargs):
    """

    :param args:
    :return:
    """

    for key, values in kwargs.items():
     print(key,":",values)

user_1 = {'Name': 'Nilam','Age': 25,'Contact No': 96572359}
wild_card_kwargs_function(**user_1)
