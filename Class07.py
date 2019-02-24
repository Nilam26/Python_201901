"""
    1) Anonymous Lambda function
2) Iterator
3) Generator
4)Iterator vs Generator
"""
"""
# ############################
# ## Anonymous Lambda function
# ############################

"""
# lambda object : operation/expression
# map(lambda object : operation /  expression, iterable object
"""

add_func = lambda ele_1, ele_2, ele_3: (ele_1 + ele_2) * ele_3
ele_1 = int(input("1st element"))
ele_2 = int(input("2nd element"))
ele_3 = int(input("3rd ele"))
print(add_func(ele_1, ele_2, ele_3))

_sq = list(map(lambda x: x * x, [1, 2, 3, 4, 5]))
print("Lambda using list",  _sq)
"""
# ############################
# ## Iterator
# ############################
"""
class MyRange:
    def __init__(self, i, n, s):
        self.i = 0
        self.n = n
        self.s = s
    def __iter__(self):
         return self

    def next(self):
        i = self.i
        if self.i < self.n:
            self.i += 1
            return i
        else:
            raise StopIteration()

data = MyRange(0, 5, 1)

print(data.next())
print(data.next())
print(data.next())
print(data.next())
"""
# ############################
# ## Generator
# ############################
"""

def simple_generator():
    yield 1
    yield 2
    yield 3

for item in simple_generator():
    print(item)

for item in range(1, 4):
    print(item)

"""

"""def fact(limit):
    #numbers = []
    initial = 1
    output = 1

    while initial <= limit:
        yield initial * output
        output, initial = initial*output, initial+1

for i in fact(5):
    print(i)

"""

def IsPrime(limit):
    flag = True
#    limit = int(input("Enter the Limit"))
    number = 2
    while number > limit:
         for j in range(2, number):
                if j % number == 0:
                 flag = True
                    break

         if flag:
            yield number, flag

k = IsPrime(12)
print("is prime")


"""

#lower = int(input("Lower Inte"))
u = int(input("upper Inte"))

for num in range(1, u + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, "IS Prime")
"""