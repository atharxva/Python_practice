# #function is a block of code which can  be called whenever needed to reduce repeated lines of code
# # A function is a block of code which only runs when it is called.
# # You can pass data, known as parameters, into a function.
# # A function can return data as a result.
# # the def keyword is used to define a function
# def my_function():
#     print("Hello from a function")

# #to call a function write the function name with a parenthesis in the end

# # Arguments
# # Information can be passed into functions as arguments.
# # Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# # The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

# def name_function(name):
#      print("Mr "+name)

# name_function("atharva")

# # when the function is called the compiler searches for the definition of the function and returns the function 
# #use tab to indent .

# #argument
# def sum(a,b):
#      return a+b

# a  = int(input("Enter the the first number"))
# b = int(input("Enter teh second number"))
# print(sum(a,b))


# #types of arguments 
# #1)position arguments
# #2) keyword arguments


# # Keyword Arguments
# # You can also send arguments with the key = value syntax.
# # This way the order of the arguments does not matter.

# def xyx(a,b):
#      print(a,b)
# xyx(a = "Atharva ",b = "garvit")
# # the sequence of the arguments doesnt matter they can be passed in any manner

# #passing  a list as an argument
# def myfun(food):
#      for x in food:
#           print(x)
# food  =  ["apple","cherry","banana"]
# (myfun(food))

# #you can use the return statment to return a particular value in a function.

# #if you want a function with no code block or no definiton you can use the pass statement in the definition
# def myfunction():
#   pass



# #dynamic argument passing
# #1)*args: when you use this method all the arguments are stored in the form of  a tuple, and has to be accessed one by one, args is not a standard name you can use any name

# def enterDetails(*args):
#     total = sum(args)
#     average = total / len(args)
    
#     print("Sum:", total)
#     print("Average:", average)

# a = int(input("Enter the input for the first number: "))
# b = int(input("Enter the input for the second number: "))
# c = int(input("Enter the input for the third number: "))
# enterDetails(a, b, c)




# # If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# lst= []
# a = int(input("Enter the number of elements"))


# for i in range(0,a):
#     lst.append(int(input("Enter the elements")))
# print(lst)

# #dry programming :dont repeat yourself


# # recursion
# # it is the method to make the function call itself
# def factorial(n):
 
# #      return (n * factorial(n - 1)) 
# # factorial = 0

# # num = (input("Enter the number"))
# # print(factorial(num))

# #2)*kwargs: Arbitrary Keyword Arguments, **kwargs
# # position based arguments should always be on the right side
# #eg

#      def fun_name(name,age):
#           y = name
#           x = age
#           z = x+y
#           print(z)
#           fun_name(age  = 32,name = "abc")

# the functions which do not return any value are called void of null functions
# print(print())
#the return type of print is null so it returns none when executed.


#dir() prints the list of variables in the scope of the function
def main():
    a = 10
    b = 55
    result = abs(a,b)
    print("absolute value of ",a,"-",b"=",result)

def abs(x,y):
    print("in function abs dir()",dir())
    z = y-x
    return z
main()
