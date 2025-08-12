# class Car:
#     def __init__(self, make, model, year, price):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.price=price

#     def display_info(self):
#         print(f"Car: {self.year} {self.make} {self.model} price is {self.price}")

# # Creating an object (instance) of the Car class
# my_car = Car("Toyota", "Corolla", 2021, 500000000)

# car1 = Car("Honda", "Civic", 2022, 5000000)
# car2= Car("ford", 'mustang', 2001, 7000000)
# car1.display_info()
# car2.display_info()


# # Accessing object methods
# my_car.display_info()



# class Dog:
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name

#     def bark(self):
#         print(f"{self.name} says woof!")

# # Creating an object

# dog1 = Dog("Labrador", "Buddy")
# dog1.name = "Max"  # Changing the dog's name 
# dog1.bark()  

# Accessing methods
# dog1.bark()  
# print(dog1)
# print(dog1.) 


# Parent class (Base class)
# class Animal:
#     def __init__(self, name):  # ✅ Constructor (used by all child classes)
#         self.name = name

#     def sound(self):  # ✅ Method to be overridden in child classes
#         pass

# # Child class (Derived class)
# class Dog(Animal):  # ✅ Inheriting from Animal
#     def sound(self):  # ✅ Overriding parent method
#         return f"{self.name} says woof!"

# # Creating an instance of Dog
# dog = Dog("Buddy")  # ✅ Inherits name from Animal's __init__

# # Calling the method
# print(dog.sound())  # ✅ Calls the overridden method




# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __str__(self):
#         return f"'{self.title}' by {self.author}"

    # def  abc(self):
    #     print(f"{self.title} by {self.author}")

# book = Book("1984", "George Orwell")
# print(book)  
# print(book.abc())

#inheritance

# class Person:
#     def __init__(self,name,contact):
#         self.name=name
#         self.contact=contact

#     def address(self):
#         print(f"{self.name} {self.contact}")

# class Doctor(Person):
#     pass

# class Patient(Person):
#     pass

# doc1=Doctor("abc", 101)
# pat1=Patient("abc",98576446654)

# doc1.address()
# pat1.address()

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def sound(self):
#         return f"{self.name} says boww"

# class Dog(Animal):
#     def sound(self):
#         return f"{self.name} says woof!"

# dog = Dog("Buddy")
# print(dog.sound())  


#@staticmethod keeps related functions organized inside the class, even if they don’t use self (instance) or cls (class)

# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return (celsius * 9/5) + 32

# print(TemperatureConverter.celsius_to_fahrenheit(37))

# class Book: 
#     def __init__(self, title, author): 
#         self.title = title 
#         self.author = author 
#     def __str__(self): 
#         return f"'{self.title}' by {self.author}" 
# book = Book("1984", "George Orwell") 
# print(book)


# class Company: 
#     company_name = "Tech Innovators" 
#     @classmethod 
#     def change_company_name(cls, new_name): 
#         cls.company_name = new_name 
# # Change class variable through class method 
# Company.change_company_name("Future Solutions") 
# print(Company.company_name) 


# class MathOperations: 
#     @staticmethod 
#     def add(a, b): 
#      return a + b 
# print(MathOperations.add(10, 20)) 

# ✔ Benefits of Using @staticmethod Instead of a Regular Function:

# Organizes related functions inside a class (especially for utility functions).

# Makes it clear that the function belongs to the class’s purpose.

# Prevents accidental modifications of instance (self) or class (cls) attributes.

# Can be accessed without creating an object, unlike instance methods.




# ✔ It still works because Python treats add() as a regular function inside the class.
# ❌ But it does not behave like a typical instance or class method




# class Animal: 
#     def __init__(self, name): 
#         self.name = name 
#     def sound(self): 
#         pass 
# class Dog(Animal): 
#     def sound(self): 
#         return f"{self.name} says woof!" 
# dog = Dog("Buddy") 
# print(dog.sound()) 



# class Employee:
#     def __init__(self, name, salary):
#         self.name = name  # Public attribute
#         self.__salary = salary  # Private attribute

#     def display_employee(self):
#         print(f"Name: {self.name}, Salary: {self.__salary}")

#     def update_salary(self, new_salary):
#         self.__salary = new_salary

# #  Creating an Employee object
# emp = Employee("John", 50000)
# emp.display_employee() 

    
# print(emp.__salary)
# print(emp.name)
# emp.update_salary(60000)
#emp.display_employee()




# class Engine: 
#     def start_engine(self): 
#         print("Engine started.") 
# class Wheels: 
#     def rotate(self): 
#         print("Wheels are rotating.") 
# class Car(Engine, Wheels):  # Car inherits from both Engine and 
#     def drive(self): 
#      print("Car is driving.") 
# car = Car() 
# car.start_engine() 
# car.rotate()        
# car.drive()   



#Example (Hierarchical Inheritance): Multiple classes inherit from the same parent class. 
# class Animal: 
#     def speak(self): 
#         print("Animal speaks.") 
# class Dog(Animal): 
#     def speak(self): 
#         print("Dog barks.") 
# class Cat(Animal): 
#     def speak(self): 
#         print("Cat meows.") 
# dog = Dog() 
# cat = Cat() 
# dog.speak()  
# # cat.speak() 



# class Animal: 
#     def speak(self): 
#         print("Animal makes a sound.") 
# class Dog(Animal): 
#     def speak(self): 
#         print("Dog says Woof!") 
# class Cat(Animal): 
#     def speak(self): 
#         print("Cat says Meow!") 
# animals = [Dog(), Cat()] 
# for a in animals: 
#     a.speak()


from abc import ABC, abstractmethod 
class Shape(ABC):  # Abstract class 
    @abstractmethod 
    def area(self): 
        pass 
class Rectangle(Shape): 
    def __init__(self, width, height): 
        self.width = width 
        self.height = height 
    def area(self): 
        return self.width * self.height 
# Cannot instantiate abstract class 
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape 
rectangle = Rectangle(10, 20) 
print(rectangle.area())


# from abc import ABC, abstractmethod  # Import abstract base class module

# # Abstract class
# class Shape(ABC):  
#     @abstractmethod
#     def area(self):  # Abstract method (must be implemented in subclasses)
#         pass  

# # Subclass (Must implement 'area()')
# class Rectangle(Shape):  
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):  # Implementing the abstract method
#         return self.width * self.height

# # Subclass (Must implement 'area()')
# class Circle(Shape):  
#     def __init__(self, radius):
#         self.radius = radius

#     def area1(self):  # Implementing the abstract method
#         return 3.14 * self.radius * self.radius
    
# class Triangle(Shape):  # ❌ Does not implement 'area()'
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

    

# triangle = Triangle(5, 10) 
# print(triangle.base*triangle.height)

# #Cannot create an instance of an abstract class
# # shape = Shape()  # ❌ ERROR: Can't instantiate abstract class

# # # Creating instances of concrete subclasses
# rectangle = Rectangle(10, 5)
# # circle = Circle(7)

# print(rectangle.area())  # ✅ Output: 50
# # print(circle.area())     # ✅ Output: 153.86



# class Person: 
#     def __init__(self, name, age): 
#         self.name = name 
#         self.age = age 
#         print(f"{self.name} has been created.") 
#     def __del__(self): 
#         print(f"{self.name} has been destroyed.") 
# # Creating and destroying objects 
# p1 = Person("John", 30)  # Output: John has been created. 


# try:
#     print(p1.name) 
# except NameError:
#     print("p1 no longer exists.")



# class Employee: 
#     company = "ABC Corp"  # Class variable 
# def __init__(self, name, position): 
#     self.name = name  # Instance variable 
#     self.position = position  # Instance variable 
# emp1 = Employee("John", "Manager") 
# emp2 = Employee("Alice", "Developer") 
# # Accessing class variable 
# print(emp1.company)  # ABC Corp 
# print(emp2.company)  # ABC Corp 
# # Accessing instance variable 
# print(emp1.name)  
# print(emp2.name) h


# class Employee: 
#     def __init__(self, name, salary): 
#         self.name = name        
#         self.__salary = salary  # Private attribute 
#     def display_employee(self): 
#         print(f"Name: {self.name}, Salary: {self.__salary}") 
#     def update_salary(self, new_salary): 
#         self.__salary = new_salary 
# emp = Employee("John", 50000) 
# emp.display_employee() 
# print(emp.__salary) 
# # Correct way to update and access private attribute 
# emp.update_salary(60000) 
# emp.display_employee() 


# class Calculator: 
#     @staticmethod 
#     def add(a, b): 
#         return a + b 
# result = Calculator.add(5, 10) 
# print(result) 

# class Student: 
#     school_name = "ABC High School" 
#     @classmethod 
#     def change_school_name(cls, new_name): 
#         cls.school_name = new_name 
# Student.change_school_name("XYZ International School") 
# print(Student.school_name) 



# class Employee: 
#     company = "ABC Corp"  # Class variable 
#     def __init__(self, name, position):         
#         self.name = name  # Instance variable 
#         self.position = position  # Instance variable 
# emp1 = Employee("John", "Manager") 
# emp2 = Employee("Alice", "Developer") 
# # Accessing class variable 
# print(emp1.company)  # ABC Corp 
# print(emp2.company)  # ABC Corp 
# # Accessing instance variable 
# print(emp1.name)  # John 
# print(emp2.name) 



# class Book: 
#     def __init__(self, title, author): 
#         self.title = title 
#         self.author = author 
#     def __str__(self): 
#         return f"'{self.title}' by {self.author}" 
# book = Book("1984", "George Orwell") 
# print(book) 


# class Student: 
#     school_name = "ABC High School" 
#     @classmethod 
#     def change_school_name(cls, new_name): 
#         cls.school_name = new_name 
# Student.change_school_name("XYZ International School") 
# print(Student.school_name)  




#Duck Typing

# class Cat:
#     def speak(self):
#         print("meow")

# class Dog:
#     def speak(self):
#         print("woof")

# class Cow:
#     def moo(self):
#         print("moo")

# def make_noice(animal):
#     try:
#         animal.speak()
#     except AttributeError:
#         print("Animal does not speak")


# cat = Cat()
# dog = Dog()
# cow = Cow()

# make_noice(cat)  
# make_noice(dog)
# make_noice(cow)