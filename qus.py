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
#             print(j, end=" ")
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

# N = 4
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


#Triggering PermissionError in File Handling 
# try:
#     with open("output.txt", "w") as file:
#         file.write("Hello World")
#         print("File written successfully!")
# except PermissionError:
#     print("Permission denied!")



#logica
# def longest_consecutive(nums):
#     num_set = set(nums)  
#     longest = 0         

#     for num in num_set:  # Step 3
#         # Only start from numbers that are the start of a sequence
#         if num - 1 not in num_set:
#             current_num = num
#             current_streak = 1

#             # Count how far the sequence goes
#             while current_num + 1 in num_set:
#                 current_num += 1
#                 current_streak += 1

#             #  Update the longest streak found
#             longest = max(longest, current_streak)

#     return longest  

# nums_input_str = input("Enter numbers ")
# numlist = list(map(int, nums_input_str.split()))
# print(longest_consecutive(numlist))



#Reverse Digits of Each Element in an Array
#using built-in functions
# def reverse_digits(arr):
#     reversed_arr=[]
#     for num in arr:
#         reversed_num= int(str(num)[::-1])
#         reversed_arr.append(reversed_num)
#     return reversed_arr
# # Example usage
# arr = [12, 23, 54,10]   
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
# arr = [12,27,22,23]
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
#     for i in range(n , 0, -1):
#         stars = '*' * i
#         spaces = ' ' * (2 * (n - i))
#         print(stars + spaces + stars)

# # Example usage
# butterfly_pattern(4)



# for i in range(5):
#     for j in range(9):

#         if j == i * 2 or j == (9 - 1) - i * 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# 🐍 Personal Expense Tracker
# Console-based project

# import os

# expenses = []  # to store all expenses


# def add_expense():
#     amount = float(input("Enter amount: "))
#     category = input("Enter category (Food/Travel/Shopping/Other): ")
#     date = input("Enter date (YYYY-MM-DD): ")
#     expense = {"amount": amount, "category": category, "date": date}
#     expenses.append(expense)
#     print("✅ Expense added successfully!")


# def view_expenses():
#     if not expenses:
#         print("No expenses recorded yet.")
#         return
#     print("\n---- All Expenses ----")
#     print(f"{'Amount':<10} {'Category':<15} {'Date':<10}")
#     print("-" * 35)
#     for exp in expenses:
#         print(f"{exp['amount']:<10} {exp['category']:<15} {exp['date']:<10}")


# def search_expenses():
#     if not expenses:
#         print("No expenses recorded yet.")
#         return
#     choice = input("Search by category or date? (c/d): ").lower()
#     if choice == "c":
#         cat = input("Enter category: ")
#         results = [exp for exp in expenses if exp["category"].lower() == cat.lower()]
#     elif choice == "d":
#         dt = input("Enter date (YYYY-MM-DD): ")
#         results = [exp for exp in expenses if exp["date"] == dt]
#     else:
#         print("Invalid choice!")
#         return

#     if results:
#         print("\n---- Search Results ----")
#         print(f"{'Amount':<10} {'Category':<15} {'Date':<10}")
#         print("-" * 35)
#         for exp in results:
#             print(f"{exp['amount']:<10} {exp['category']:<15} {exp['date']:<10}")
#     else:
#         print("No matching expenses found.")


# def show_total():
#     total = sum(exp["amount"] for exp in expenses)
#     print(f"\n💰 Total Spent: {total}\n")


# def save_to_file():
#     with open("expenses.txt", "w") as f:
#         for exp in expenses:
#             f.write(f"{exp['amount']},{exp['category']},{exp['date']}\n")


# def load_from_file():
#     if os.path.exists("expenses.txt"):
#         with open("expenses.txt", "r") as f:
#             for line in f:
#                 amount, category, date = line.strip().split(",")
#                 expenses.append({"amount": float(amount), "category": category, "date": date})


# # ---- Main Program ----
# load_from_file()

# while True:
#     print("\n===== Personal Expense Tracker =====")
#     print("1. Add Expense")
#     print("2. View All Expenses")
#     print("3. Search Expenses")
#     print("4. Show Total Spent")
#     print("5. Exit")
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         add_expense()
#     elif choice == "2":
#         view_expenses()
#     elif choice == "3":
#         search_expenses()
#     elif choice == "4":
#         show_total()
#     elif choice == "5":
#         save_to_file()
#         print("Goodbye! Data saved to expenses.txt ✅")
#         break
#     else:
#         print("Invalid choice! Please try again.")



# 🐍 To-Do List Manager
# Simple console-based program

# tasks = []  # list to store tasks


# def add_task():
#     task_desc = input("Enter task description: ")
#     task = {"description": task_desc, "status": "Pending"}
#     tasks.append(task)
#     print("✅ Task added successfully!")


# def view_tasks():
#     if not tasks:
#         print("No tasks available.")
#         return
#     print("\n---- To-Do List ----")
#     for i, task in enumerate(tasks, start=1):
#         print(f"{i}. {task['description']} - {task['status']}")


# def mark_task_done():
#     view_tasks()
#     if not tasks:
#         return
#     try:
#         num = int(input("Enter task number to mark as Completed: "))
#         if 1 <= num <= len(tasks):
#             tasks[num - 1]["status"] = "Completed"
#             print("✅ Task marked as completed!")
#         else:
#             print("Invalid task number!")
#     except ValueError:
#         print("Please enter a valid number.")


# # ---- Main Program ----
# while True:
#     print("\n===== To-Do List Manager =====")
#     print("1. Add Task")
#     print("2. View All Tasks")
#     print("3. Mark Task as Done")
#     print("4. Exit")
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         add_task()
#     elif choice == "2":
#         view_tasks()
#     elif choice == "3":
#         mark_task_done()
#     elif choice == "4":
#         print("Goodbye! 👋")
#         break
#     else:
#         print("Invalid choice! Please try again.")



# Find Missing Numbers in an Array
# def find_missing_numbers(nums, n):
#     missing = []
#     for i in range(1, n + 1):
#         if i not in nums:   
#             missing.append(i)
#     return missing


# # Example 1
# nums =[1, 5, 7, 9]
# n = 6
# print("Missing numbers:", find_missing_numbers(nums, n)) 


# another example
# def find_multiple_missing(arr, n):
#     full_set = set(range(1, n + 1))   # {1,2,...,n}
#     arr_set = set(arr)                # unique elements from arr
#     missing = list(full_set - arr_set)  # numbers not in arr
#     missing.sort()  # sort the result
#     return missing
# print(find_multiple_missing([1, 3, 5, 6], 6))


# Anagram Check
# def check(s1,s2):
#     if sorted(s1) == sorted(s2):
#         print("anagram")
#     else:
#         print("not anagram")

# s1 = input("enter string 1")
# s2 = input("enter string 2")
# check(s1, s2)


#Word Frequency Counter
# def word_count(sentence):
#     words = sentence.split()
#     freq = {}

#     for word in words:
#         word = word.lower()  
#         if word in freq:
#             freq[word] += 1
#         else:
#             freq[word] = 1

#     return freq

# # Example
# sentence = "the cat and the dog"
# print(word_count(sentence))


#Decimal → Binary conversion
# def decimal_to_binary(n):
#     if n == 0:
#         return "0"
    
#     binary_digits = []
    
#     while n > 0:
#         remainder = n % 2
#         binary_digits.append(str(remainder))  # store remainder
#         n = n // 2   # integer division
    
#     # reverse because we collected from bottom to top
#     binary_digits.reverse()
    
#     return "".join(binary_digits)


# # Example usage
# num = 10
# print(f"Decimal: {num} -> Binary: {decimal_to_binary(num)}")



n = int(input())
size = 2*n - 1

for i in range(size):
    row = []
    for j in range(size):
        # Distance from the closest border
        top = i
        left = j
        bottom = size - 1 - i
        right = size - 1 - j
        # The layer number is n minus the minimum distance
        num = n - min(top, left, bottom, right)
        row.append(str(num))
    print(" ".join(row))

top =0
left =0
bottom =size-1-0
right =size-1-0
num=3-min(0,0,1,1)=2