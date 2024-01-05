#protected member functions can be accessed in the derived class 
#the data members sotre the attributes
#to operate on the attributes we use member functions
#a class is a user defined datatype
#types of ihr=eritence  1)single  2)Multiple 3)multilevel 4)heirarchial
#Eg code
# class Parent():

#     def add(self,x,y):
#         return x+y
# class Child(Parent):
#     def takevalue(self):
#         x = int(input("Enter the value of x"))
#         y = int(input("Enter the value of y"))
#         result=self.add(x,y)
#         print(result)
# c = Child()
# c.takevalue()

#program to calculate are of square using inheritance
#single inheritance
# class asking():
#     def square(self, a):
#         return a ** 2

#     def rectangle(self, x, y):
#         return x * y

# class cal(asking):
#     def area(self):
#         self.a = int(input("Enter the side: "))
#         result = self.square(self.a)
#         print(result)

#     def areas(self):
#         self.x = int(input("Enter length : "))
#         self.y = int(input("Enter the breath : "))
#         result = self.rectangle(self.x, self.y)
#         print(result)

# choice = int(input("Enter your choice which calculation you want to perform 1.square / 2. rectangle : "))
# if choice == 1:
#     obj = cal()
#     obj.area()
# elif choice == 2:
#     obj = cal() 
#     obj.areas()
# else:
#     print("some error occurred!")



#multiple inheritance: this type of inheritance has multiple parent class and onechild class
#program to list the subjects in lu and itm university
# class ITM():
#     def itm_sub(self,subi):
#      self.subi = ["management","hotel management"]
#      print(self.subi)
# class Lu():
#     def lu_sub(self,subl):
#         self.subl = ["Data management","aiml"]
#         print(self.subl)

# class con(ITM,Lu):
#    def con(self,subl,subi):
#       self.itm_sub()
#       self.lu_sub()
#       result = self.subi + self.subl
#       print(result)

class atharva:
    def _init_(self, grandfather_assets):
        self.grandfather_assets = grandfather_assets

    def display_grandfather_assets(self):
        print(f"Grandfather's Assets: ${self.grandfather_assets}")


class patil(atharva):
    def _init_(self, grandfather_assets, father_assets, father_income):
        super()._init_(grandfather_assets)
        self.father_assets = father_assets
        self.father_income = father_income

    def calculate_total_assets(self):
        total_assets = self.grandfather_assets + self.father_assets + self.father_income
        return total_assets

    def display_father_assets(self):
        print(f"Father's Assets: ${self.calculate_total_assets()}")
        print(f"Father's Income: ${self.father_income}")


class mahajan(patil):
    def _init_(self, grandfather_assets, father_assets, father_income, son_assets):
        super()._init_(grandfather_assets, father_assets, father_income)
        self.son_assets = son_assets

    def display_total_assets(self):
        total_assets = self.calculate_total_assets() + self.son_assets
        print(f"Son's Total Assets: ${total_assets}")
        print(f"Son's Assets: ${self.son_assets}")


# Example usage
grandfather_assets = int(input("Enter Grandfather's asset: "))
father_assets = grandfather_assets
father_income =int(input("Enter Father's Income: "))
son_assets = int(input("Enter Son's asset: "))



grandfather = atharva(grandfather_assets)
father = patil(grandfather_assets, father_assets, father_income)
son = mahajan(grandfather_assets, father_assets, father_income, son_assets)

grandfather.display_grandfather_assets()
print("\n")
father.display_father_assets()
print("\n")
son.display_total_assets()




