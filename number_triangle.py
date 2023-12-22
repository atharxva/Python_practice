r = int(input("Enter the number of rows"))

#1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
for row in range(0,r):
    for col in range(0,row):
        print(col+1,end =" ")
    print("\n")




