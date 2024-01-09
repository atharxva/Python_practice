import math
#incremental Development:
# a basic function to calculate the distance between two points
#formula = 
def dist(x1,x2,y1,y2):
    x1 = int(input("Enter the value of x1: "))
    x2 = int(input("Enter the value of x2: "))
    y1 = int(input("Enter the value of y1: "))
    y2 = int(input("Enter the value of y2: "))
    dx = (x2 - x1)**2
    dy = (y2 - y1)**2
    distance = math.sqrt(dx + dy)
    print("Radius of the circle",distance)   

    
def cirumference(x1,y1,x2,y2):
   
    r = dist(x1,y1,x2,y2)
    print("IN CIRCLE : ",dir())
    return (2*(22/7)*r)
#we use the leap of faith while using any functions in python
