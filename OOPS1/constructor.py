class Student():
    college_name="ABC College" # class attribute
    name="anonymous" # class attribute
    def __init_(self):
        pass

    def __init__(self, name, age):
        self.name=name # object attribute
        self.age=age

    def print_info(self):
        print(f"My name is {self.name} and age is {self.age}")
### First Arguement is ALWAYS self.
### Object attributes have higher precedence than class attributes.
s1=Student("Lakshit", 23)
s1.print_info()

s2=Student("Rohit", 38)
s2.print_info()