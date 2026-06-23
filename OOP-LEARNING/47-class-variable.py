# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:

    class_year = 2027     # class variable
    num_students = 0

    def __init__(self, name, age):  # self :- refers to the current object
        self.name = name      # instance variable
        self.age = age         # instance variable
        Student.num_students += 1        

student1 = Student("Abhishek", 21)
student2 = Student("Dodo", 21)
student3 = Student("Abhilash", 22)
student4 = Student("Sandy", 27)

# print(student1.name)
# print(student1.age)
# print(student1.class_year)

# print(student2.name)
# print(student2.age)
# print(student2.class_year)


# It is prefer to access the class variable using the class rather than object of a class
# It makes it more reableable and easy to see that we are accessing a class variable
# print(Student.class_year)

# print(Student.num_students)

print(f"Graduating {Student.class_year} class has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)