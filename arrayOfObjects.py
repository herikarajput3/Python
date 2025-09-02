#Array of Objects: It is a list of objects.
#Array of Objects in Python is a list of objects where each object can be of different type.

class Student:
    name = None
    age = None
    city = None
    
    def set_details(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")

obj = []

n = int(input("Enter number of students: "))
for i in range(n):
    s = Student()
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    city = input("Enter city: ")
    s.set_details(name, age, city)
    obj.append(s)

for student in obj:
    student.get_details()