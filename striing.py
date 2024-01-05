# #strings are immutable characters 
# #strings can be accesed using indexing
# a = "ITM SKILLS UNIVERSITY"
# # print(a[0:])
# # #in slicing the last index is excluded from the operation it uses n-1
# # #interval slicing 
# # print(a[-21:])
# i =0
# while i<len(a):
#     print(a[i])
#     i+=1
#     if i==11:
#         break

def func(string,char):
    for i in range(len(string)):
        if(string[i]==char):
            print(string.count(char))
            break
a = input("Enter the string")
b = input("Enter the character to find")
func(a,b)
