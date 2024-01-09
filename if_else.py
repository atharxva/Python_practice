# An "if statement" is written by using the if keyword.

a  = 33
b = 200
if b>a:
    print(a,"is greater than ",b)   
    
 # In this example we use two variables, a and b, which are used as part ofthe if statement to test whether b is greater than a. As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater than a".

# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 200
if a>b:
    print("A is greater than b")
elif b>a:
    print("B is greater than A")


# The else keyword catches anything which isn't caught by the preceding conditions.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")



# The or keyword is a logical operator, and is used to combine conditional statements:
# Example
# Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


#   The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass

