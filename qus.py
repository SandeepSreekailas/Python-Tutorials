# num1 = float(input("Enter first number: "))
# operation = input("Enter operation (+, -, *, /): ")
# num2 = float(input("Enter second number: "))


# if operation == '+':
#     print("Result:", num1 + num2)
# elif operation == '-':
#     print("Result:", num1 - num2)
# elif operation == '*':
#     print("Result:", num1 * num2)
# elif operation == '/':
#     print("Result:", num1 / num2 if num2 != 0 else "Cannot divide by zero")
# else:
#     print("Invalid operation")


# Find the sum of first n natural numbers using while

# n = int(input("Enter a number: "))
# sum = 0 
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("Sum:", sum)


# def number_pyramid(n):
#     for i in range(n):
#         print("  " * i, end="") 
#         for j in range(1, n - i + 1):
#             print(j, end="  ")
#         print() 

# rows = int(input("Enter the number of rows: "))
# number_pyramid(rows)



# size = int(input("Enter the size of the array: "))
# print(f"Enter {size} elements:")
# arr = list(map(int, input().split()))


# if len(arr) != size:
#     print("Error: Number of elements does not match size.")
#     exit()

# largest = arr[0]
# smallest = arr[0]
# total_sum = 0
# even_numbers = []
# odd_numbers = []

# for num in arr:
#     total_sum += num
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num

#     if num % 2 == 0:
#         even_numbers.append(num)
#     else:
#         odd_numbers.append(num)

# sum_even = sum(even_numbers)
# sum_odd = sum(odd_numbers)
# count_even = len(even_numbers)
# count_odd = len(odd_numbers)

# print("Even numbers in the array:", *even_numbers)
# print("Odd numbers in the array:", *odd_numbers)
# print("Largest element:", largest)
# print("Smallest element:", smallest)
# print("Sum of all elements:", total_sum)
# print("Sum of even numbers:", sum_even)
# print("Sum of odd numbers:", sum_odd)
# print("Count of even numbers:", count_even)
# print("Count of odd numbers:", count_odd)

#Write a python program to print the following pattern: 
# def print_pattern(N):
#     for i in range(1, N + 1):
#         print("* " * (i * 2))  # print 2*i asterisks
#         if i != N:  # don't print the trailing stars after the last group
#             for j in range(i * 3):
#                 print("*")


# N = 3
# print_pattern(N)



#Write a program to print an array of random numbers in reverse order.  

# import random

# def reverse_random_array(N):
#     # Generate an array of N random integers between 1 and 100
#     arr = [random.randint(1, 100) for i in range(N)]
#     print("Original array:", arr)
    
#     # Reverse the array
#     reversed_arr = arr[::-1]
#     print("Reversed array:", reversed_arr)

# # Example usage
# N = 7
# reverse_random_array(N)


#Area of a rectangle using class and objects
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# # Example
# rect = Rectangle(5, 3)
# print("Area of the rectangle:", rect.area())


# Grade calculation using class and objects
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


# Write a Python program to demonstrate encapsulation using a BankAccount class.
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

# Trying to access private variable (will cause error)
# print(acc.__balance) 


#Q: Write a Python program to demonstrate Polymorphism using classes Bird, Parrot, and Sparrow.
# class Bird:
#     def sound(self):
#         print("Bird makes a sound")

# class Parrot(Bird):
#     def sound(self):
#         print("Parrot says 'Hello'")

# class Sparrow(Bird):
#     def sound(self):
#         print("Sparrow chirps")

# # Function that uses polymorphism
# def make_sound(bird):
#     bird.sound()

# # Using the function
# b1 = Parrot()
# b2 = Sparrow()

# make_sound(b1) 
# make_sound(b2)  # Output: Sparrow chirps


#error handling questions
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a / b
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")
# except ValueError:
#     print("Error: Please enter valid integers.")


#File Handling Reading from a File
# try:
#     with open("sample.txt", "r") as file:
#         content = file.read()
#         print("File Content:\n", content)
# except FileNotFoundError:
#     print("Error: File does not exist.")


#Combining Error & File Handling
# try:
#     filename = input("Enter filename to read: ")
#     with open(filename, "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("Error: File not found.")


#logica
# def longest_consecutive(nums):
#     num_set = set(nums)  # Step 1
#     longest = 0          # Step 2

#     for num in num_set:  # Step 3
#         # Step 4: Only start from numbers that are the start of a sequence
#         if num - 1 not in num_set:
#             current_num = num
#             current_streak = 1

#             # Step 5: Count how far the sequence goes
#             while current_num + 1 in num_set:
#                 current_num += 1
#                 current_streak += 1

#             # Step 6: Update the longest streak found
#             longest = max(longest, current_streak)

#     return longest  # Step 7
# nums = [100,101,102,1,2,3]
# print(longest_consecutive(nums)) 


#Reverse Digits of Each Element in an Array
#using built-in functions
# def reverse_digits(arr):
#     reversed_arr=[]
#     for num in arr:
#         reversed_num= int(str(num)[::-1])
#         reversed_arr.append(reversed_num)
#     return reversed_arr
# # Example usage
# arr = [12, 23, 54]   
# result = reverse_digits(arr)
# print("Original array:", arr)
# print("Reversed array:", result)

#without using built-in functions
# def reverse_digits(arr):
#     reversed_arr = []
#     for num in arr:
#         reversed_num = 0
#         while num > 0:
#             reversed_num = reversed_num * 10 + num % 10 
#             num //= 10
#         reversed_arr.append(reversed_num)
#     return reversed_arr

# # Example usage
# arr = [12,20,22,23]
# result = reverse_digits(arr)
# print("Original array:", arr)
# print("Reversed array:", result)


# Butterfly Pattern

# def butterfly_pattern(n):
#     # Top half
#     for i in range(1, n + 1):
#         stars = '*' * i
#         spaces = ' ' * (2 * (n - i))
#         print(stars + spaces + stars)
    
#     # Bottom half
#     for i in range(n, 0, -1):
#         stars = '*' * i
#         spaces = ' ' * (2 * (n - i))
#         print(stars + spaces + stars)

# # Example usage
# butterfly_pattern(4)



for i in range(5):
    for j in range(9):

        if j == i * 2 or j == (9 - 1) - i * 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()