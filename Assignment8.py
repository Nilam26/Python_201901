
list1 = [2, 0, 7, 4, 1]
for i in range(0, 10):
    minimum = list1[0]
    maximum = list1[0]
    for j in list1:
        if j < minimum:
            minimum = j

        else:
            if j > maximum:
                maximum = j


print("Minimum no is:", minimum)
print("Maximum no is:", maximum)