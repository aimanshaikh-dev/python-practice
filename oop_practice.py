#Classes + Objects + Constructor

class Student:
    college = "Amity university"


    def __init__(self, name , age):
        self.name = name
        self.age = age
        
    def intro(self):
        return f'HI , i am {self.name}, age {self.age}, college {Student.college}'
    

s1 = Student("Aiman", 20)
s2 = Student("John", 21)

print(s1.intro())
print(s2.intro())


#Inheritance + Polymorphism

class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


animals = [Dog(), Cat(), Animal()]
for a in animals:
    print(a.speak())


# Method overriding

class Parent:
    def show(self):
        return "Parent show()"


class Child(Parent):
    def show(self):
        return "Child show() overridden"


c = Child()
print(c.show())



