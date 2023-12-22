r = int(input("Enter the number of rows"))

for row in range(0,r):
    for col in range(0,row):
        print("*",end=" ")
    print('\r')
    
for row in range(r,0,-1):
    for col in range(0,row):
     print("*",end = " ")

    print('\n')