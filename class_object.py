#classes are the blueprint of objects.
#class consists of data members and member functions.
#the class attributes are the same for all obejcts.
#python doesnt support method overloading
#define class with the reserved keyword class
#by default the data is public in python
#syntax for encapsulation
#public : xyz
#private: _xyz
#private: __xyz

#the same syntax will be used to member functions and their access specifiers
class Student:
    count = 0
    def __init__(self):
        self.name = input("Enter the name: ")
        self.age = int(input("Enter the age: "))
        self.department = input("Enter the department (PGDM(p)/B.Tech(b)): ").capitalize()
        Student.count += 1
    def __del__(self):
        print("Destructor is invoked")

    def display(self):
        print("Name:", self.name, "Age:", self.age, "Department:", self.department)
print("""
STUDENT ADMIT
------------------""")
pgdm_students = []
btech_students = []
num_students = int(input("Enter the number of students: "))
for _ in range(num_students):
    new_student = Student()
    new_student.display()
    if new_student.department == 'PGDM ':
        pgdm_students.append(new_student)
    elif new_student.department == 'B.TeCH':
        btech_students.append(new_student)
print("*******")
print("\nPGDM Department Students:")
for student in pgdm_students:
    student.display()

print("\nB.Tech Department Students:")
for student in btech_students:
    student.display()

print("\nTotal number of students:", Student.count)


#the constructer and destructor is only called when an object is created and they are execued regardless of the sequence of the definition, destructor has no parmeters


