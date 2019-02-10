"""

Today`s  Topic
1) Conditional statement
2)Break and Continue
3)Looping Structure
4)Nested Loop
5)
"""

# ################3
# 1) Conditional statement
# ##################3

# if
""""
if<Condition>:
        Statement // tab
   """""
number_01 = 4
number_02 = 8
number_03 = 6

if number_01 < number_02:
    print("number 2 is greater than number 1")


# if else
if number_01 > number_02:
    print("number 1 is greater than number 2")
else:
    print("number 2 is greater than number 1")

# if elif else

if number_01 < number_02:
    print("number 1 is greater than number 2")
elif number_02 < number_03:
    print("number 3 is greater than number 2")
else:
    print("number 2 is greater than number 1")

# Nested if else
if number_01 > number_02:
    if number_01 > number_03:
        print("---num 1 is max")
    else:
        print("num 3 is max")
else:
        if number_02 > number_03:
            print("num 2 is max")
        else:
                print("num 3 is max")

if number_01 < number_02 < number_03:
    print("num 3 is max")
elif number_01 < number_02 and number_02 > number_03:
    print("Num 2 is max")
elif number_01 > number_02 and number_01 > number_03:
    print("Num 1 is max")

# ################3
#  2)Break and Continue
# ##################3

# #####
# 3)Looping Structure
# ########3
# for
# while
"""
for i in range(0, 5, 1) // i stand for iterable format 
print (i)
"""
for i in range(5, 5):
    for j in range(0, i):
        print(j, end=" ")
    print('')

for i in range(0,  5):
    for j in range(0, 5):

        print("*", end=" ")
    print('')

for i in range(0,  5):
    for j in range(0, 5):

        print("1", end=" ")
    print('')

for i in range(0,  5):
    for j in range(0, 5):
        print(i % 2, end=" ")
    print('')


# while loop
# ##number = 0
# ##while number < 5:
# ##    print(number)
# ##   number += 1

# ##for i in range(0, 11, 2):
# ##if i % 2  == 0:
# ##        print(i, end=" ")
# ##        print('')

# ##do while loop (by default enter in loop)


  # number = 0
   #     while True:
    #        if number > 5:
     #           break
      #          print(number)
       #         number += 1




