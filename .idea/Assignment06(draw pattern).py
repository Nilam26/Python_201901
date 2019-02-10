"""
0
10
010
1010
01010
"""

for i in range(0,5):
    for j in range(0,5):
        if(i>=j):
            #if(i==j):
                #print("test",end="")
            #else:
                x = j - i
                if (x % 2 == 0):
                    print("0", end="")
                else:
                    print("1", end="")
    print("")


"""
12345
12345
12345
12345
12345
"""
print("----------------------------------")
print("ASSIGNMENT 6")
print("----------------------------------")
for i in range(1,6):
    for j in range(1,6):

            print(j,end="")
    print("")


"""
2
24
248
24816
2481632
"""
print("----------------------------------")
print("ASSIGNMENT 12")
print("----------------------------------")
for i in range(1,7):
    for j in range(1,7):

        if(i>=j):
         print(j ** 2,end="")

    print("")

"""
1
10
101
1010
10101
"""
print("---------------")
print("Assignment 5")
print("---------------")
for i in range(1,6):
    for j in range(1,6):
        if(i>=j):
            x = i-j
            if(j %2==0):
                print("0",end="")
          #  print("")
            else:
                print("1",end="")
    print("")


"""
10101
0101
101
01
1    
"""
print("---------------")
print("Assignment 8")
print("---------------")
for i in range(1, 6):
    for j in range(1, 6):
        if (i<= j):
            x = i - j
            if (j % 2 == 0):
                print("0", end="")
            #  print("")
            else:
                print("1", end="")
    print("")

print("---------------")
print("Assignment 11")
print("---------------")

for i in range(1,6):
    for j in range(1,6):

        print(j*i ,end="")
    print("")

print("---------------")
print("Assignment 9")
print("---------------")

for i in range(1,5):
    for j in range(1,5):
        if(i>=j):
            j =  j - 2
            if(j%2  !=  0):
                print( "1",end="")
            else:
                print("",end="")
    print("")

    print("---------------")
    print("Assignment 7")
    print("---------------")




for i in range(1,6):
  for j in range(1,6):
   #if(i<=j):
    n = 0
    while (n<=25):
     n=n+1
     #j=n
    print(j,end="")
  print("")

"""
 1      
  1 1    
 1 1 1  
1 1 1 1
"""
print("---------------")
print("Assignment 11")
print("---------------")

for i in range(1,5):
    for j in range(1,11):
        if(i<=j):
            if (i== 1 and j==4) or (i == 2 and j == 4) or (i == 2 and j == 6) or (i == 3 and j == 2) or (i == 3 and j == 4) \
                or (i == 3 and j == 6) or (i == 3 and j == 8) or (i == 4 and j == 8) or (i == 4 and j == 2) or \
                    (i == 4 and j == 4) or (i == 4 and j == 6) or (i == 4 and j == 10):
                print("1",end="")

            else:
                print(" ",end="")
    print("")

print("------------------")
print("Assignment 15")
print("------------------")
for i in range(1,6):
    for j in range(1,6):
        if(i <= j):
            print("1",end="")
        else:
            print(" ",end="")
    print("")

    print("----------------------------------")
    print("ASSIGNMENT 6")
    print("----------------------------------")
    n = 0
    for i in range(1, 6):
        for j in range(1, 6):

            if(j<6):
                if(n<27):
                    n=n+1
                    j=n
                    print(str(j).zfill(2), end="")
            #j=j+1
        print("")

print("----------------------------------")
print("ASSIGNMENT 10")
print("----------------------------------")
n=2
x=4
y=5
for i in range(1, 6):
    for j in range(1, 6):

        if(j==1 or j==5) or i==j and  j!=4 or (i == 2 and j == 4):
             print("*",end="")
        else:

             print(" ",end="")
    print("")


print("----------------------------------")
print("ASSIGNMENT 13")
print("----------------------------------")
n=2
x=4
y=5
for i in range(1, 6):
    for j in range(1, 8):

        if(j==1 or j==7)  or i==1 and (j!=3 and  j!=4 and j!= 5) or (i==3 and j==4) or (i == 2 and j == 3 ) \
                or (i == 2 and j == 5) :
             print("*",end="")
        else:

             print(" ",end="")
    print("")
