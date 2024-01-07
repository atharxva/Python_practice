# class Person:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# p = Person("Atharva",18)
# print(p.name)
# print(p.age)


class Person:
    def __init__(self,name,age):
        self.name =  name
        self.age = age
    def display(self):
        print("MY name is ",self.name," and my age is ",self.age)


a = input("Enter your name")
b = int(input("Enter your age"))
p = Person(a,b)
p.display()