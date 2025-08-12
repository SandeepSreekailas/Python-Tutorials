# 1. Grade Calculation using Class and Objects

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display_grade(self):
#         if self.marks >= 90:
#             grade = "A"
#         elif self.marks >= 75:
#             grade = "B"
#         elif self.marks >= 50:
#             grade = "C"
#         else:
#             grade = "Fail"
#         print(f"{self.name}'s Grade: {grade}")

# # Example
# s1 = Student("John", 92)
# s2 = Student("Alice", 78)
# s2.display_grade()
# s1.display_grade()



# 2. Encapsulation Example (Bank Account)

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited Rs {amount}")
#         else:
#             print("Invalid amount")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew Rs {amount}")
#         else:
#             print("Insufficient balance")

#     def get_balance(self):
#         return self.__balance

# acc = BankAccount("Alice", 1000)
# acc.deposit(500)
# acc.withdraw(200)
# print("Final Balance:", acc.get_balance())
# print(acc.__balance)  # Will cause error


# 3. Polymorphism Example (Birds)

# class Bird:
#     def sound(self):
#         print("Bird makes a sound")

# class Parrot(Bird):
#     def sound(self):
#         print("Parrot says 'Hello'")

# class Sparrow(Bird):
#     def sound(self):
#         print("Sparrow chirps")

# def make_sound(bird):
#     bird.sound()

# b1 = Parrot()
# b2 = Sparrow()
# make_sound(b1)
# make_sound(b2)


# 4. Library Book Management

# class Book:
#     def __init__(self, title, author, copies):
#         self.title = title
#         self.author = author
#         self.copies = copies

#     def display_info(self):
#         print(f"Title: {self.title} | Author: {self.author} | Copies: {self.copies}")

# books = []
# for i in range(3):
#     title = input("Enter book title: ")
#     author = input("Enter author: ")
#     copies = int(input("Enter copies: "))
#     books.append(Book(title, author, copies))

# search_title = input("Enter book title to search: ")
# found = False
# for book in books:
#     if book.title.lower() == search_title.lower():
#         book.display_info()
#         found = True
#         break
# if not found:
#     print("Book not available")


# 5. Employee Bonus

# class Employee:
#     def __init__(self, name, position, salary):
#         self.name = name
#         self.position = position
#         self.salary = salary

#     def apply_bonus(self, percentage):
#         self.salary += self.salary * (percentage / 100)

#     def display_info(self):
#         print(f"Name: {self.name} | Position: {self.position} | Salary: {self.salary}")

# employees = []
# for i in range(2):
#     name = input("Enter name: ")
#     position = input("Enter position: ")
#     salary = float(input("Enter salary: "))
#     emp = Employee(name, position, salary)
#     bonus = float(input("Enter bonus %: "))
#     emp.apply_bonus(bonus)
#     employees.append(emp)

# for emp in employees:
#     emp.display_info()


# 6. Shopping Cart

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# class Cart:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product):
#         self.products.append(product)

#     def total_price(self):
#         return sum(p.price for p in self.products)

# cart = Cart()
# for i in range(3):
#     name = input("Enter product name: ")
#     price = float(input("Enter price: "))
#     cart.add_product(Product(name, price))

# print("Total price: Rs", cart.total_price())


# 7. Movie Ticket Booking

# class Movie:
#     def __init__(self, title, available_seats):
#         self.title = title
#         self.available_seats = available_seats

#     def book_ticket(self, seats):
#         if seats <= self.available_seats:
#             self.available_seats -= seats
#             print(f"{seats} tickets booked successfully.")
#         else:
#             print("Not enough seats.")

# title = input("Enter movie title: ")
# seats = int(input("Enter available seats: "))
# movie = Movie(title, seats)

# movie.book_ticket(int(input("Enter seats to book: ")))
# movie.book_ticket(int(input("Enter seats to book: ")))


# 8. Loan Eligibility

# class Customer:
#     def __init__(self, name, income, credit_score):
#         self.name = name
#         self.income = income
#         self.credit_score = credit_score

#     def check_eligibility(self):
#         if self.income >= 25000 and self.credit_score >= 650:
#             print(f"{self.name} is eligible for loan.")
#         else:
#             print(f"{self.name} is not eligible for loan.")

# name = input("Enter name: ")
# income = float(input("Enter income: "))
# credit_score = int(input("Enter credit score: "))

# cust = Customer(name, income, credit_score)
# cust.check_eligibility()


# 9. Online Order Tracking

# class Order:
#     def __init__(self, order_id, product_name, status):
#         self.order_id = order_id
#         self.product_name = product_name
#         self.status = status

# orders = []
# for i in range(2):
#     order_id = int(input("Enter order ID: "))
#     product_name = input("Enter product name: ")
#     status = input("Enter status: ")
#     orders.append(Order(order_id, product_name, status))

# print("\nUpdated Orders:")
# for order in orders:
#     print(f"{order.order_id} - {order.product_name} - {order.status}")
