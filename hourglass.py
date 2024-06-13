rows= int(input("Enter number of rows: "))
print("genrated hourglass pattern is : ")
for i in range (rows,0,-1):
    for j in range (rows -i):
        print(" " ,end=" ")
    for j in range (1,2*i):
        print("* ",end=" ")
    print()

#lower
for i in range (2,rows+1):
    for j in range (rows-i):
        print(" " ,end=" ")
    for j in range (1,2*i):
        print("* ",end=" ")
    print()