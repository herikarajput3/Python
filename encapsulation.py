class Student:
    id = None
    name = None
    age = None
# Setter function
    def set_details(self, id, name, age):
        # self refers to the instance of the class
        self.id = id
        self.name = name
        self.age = age

# Getter function
    def get_details(self):
        return self.id, self.name, self.age
    
s1 = Student()
s2 = Student()

s1.set_details(101, "Herika", 20)
s2.set_details(102, "Rutu", 21)

print(s1.get_details())
print(s2.get_details())