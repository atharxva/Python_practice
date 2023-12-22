# *****
# *   *
# *   *
# *   *
# *****

h = int(input("Enter the height"))
w =  int(input("Enter the width"))

for row in range(0,h):
    for col in range(0,w):
        if h == 0 or row == h-1 or w==0 or col==w-1:
            print("*",end = " ")
        else:
            print(" ",end = '')
    print("\r")