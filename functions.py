# def message(name):
#     print("hello world "+ name)

# message("python")




# def greet(name):
#     print(f"Hello, {name}!")
    
# greet("Alice")  

# def add(a, b,c  ):
#     return a * b * c

# print(add(3, 4, 6))


# def greet(name, msg="Good morning"):
#     print(f"{msg}, {name}!")
    
# # greet("Alice")
# greet("Bob", "Good evening")


# def greet(name,msg):  
#     print(f"{msg}, {name}!")

# greet( msg="Hello", name="ali")  

# greet("Bob", "Good evening")  


# def finde_sum():
#     return 10 + 20

# print(finde_sum())

# def finde_sum(num):
#     return num * num

# print(finde_sum(10))

# def add(a, b):
#     """This function adds two numbers."""
#     return a + b

# print(add.__doc__)
# print(add(10,20))


# add=lambda a, b: a + b
# print(add(3, 5))


# numbers = [1, 2, 3, 4]
# squared = map(lambda x: x ** 2, numbers)
# print(list(squared))

# list1=[1,2,3,4,5,6,7,8,9,10]
# def even(x):
#     if x % 2==0:
#         return x
# f=filter(even,list1)
# print(list(f))

# list1=[1,2,3,4,5,6,7,8,9,10]
# f= filter(lambda x : x%2 != 0, list1)
# print(list(f))


# numbers = [1, 2, 3, 4]
# squared = map(lambda x: x ** 2, numbers)
# print(list(squared))

# from functools import reduce
# numbers = [1, 2, 3, 4]
# sum_result = reduce(lambda x, y: x *y, numbers)
# print(sum_result)


# def increment(n):
#     return lambda x: x + n

# a = increment(5)
# print(a(15))  


# def apply_function(func, x):
#     return func(x)

# def square(x):
#     return x * x

# result = apply_function(square, 5)  # Applying the 'square' function to 5
# print(result)


# x = 10  # Global scope

# def outer_function():
#     x = 5  # Enclosing scope
#     def inner_function():
#          # Local scope
#         print(x)
  
   
#     inner_function()
# print(x)  

# outer_function()  # Output: 2
 


# def hai(*values):
#     print(values[1],values[0], values[3], values[2])
# hai('messi', 'barcelona', 'Agrentina','hellloo')


# def sum_numbers(*abcd):
#     total = 0
#     for number in abcd:
#         total += number
#     return total

# result = sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(result)


# def hai(**info):
#     print("first: " + info["first"])
#     print("second: " + info["second"])
#     print("third: " + info["third"])
    

# hai(first="messi",third="king", second="barcelona") 


# def print_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_details(name="Alice", age=30, city="New York", lcity="New uuu")


# def display_info(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# display_info(1, 2, 3,4,5, name="Alice", age=25)


# def full_function_example(param1, *args,  **kwargs):
#     print("Regular parameter:", param1)
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# full_function_example(10, 20, 30, name="Alice", age=30)


# def pali(n):
#     s=str(n)
#     left,right=0,len(s)-1

#     while left<right:
#         if s[left]!=s[right]:
#             return False
#         left+=1
#         right-=1
#         return True
    
# n=9874789
# if pali(n):
#     print("yes")
# else:
#     print("no")

# def palin(s):
#     s = s.lower()  
#     left, right = 0, len(s) - 1

#     while left < right:
#         if s[left] != s[right]:
#             return False  
#         left += 1
#         right -= 1

#     return True  

# String = input("Enter a string: ").strip()

# if not String:
#     print("No string entered")  
# elif palin(String):
#     print("Entered string is a palindrome")
# else:
#     print("Entered string is not a palindrome")

# def is_palindrome(s):
#     s = s.lower()  
#     return s == s[::-1]

# # Example usage
# word = input("Enter a word: ").strip()
# if is_palindrome(word):
#     print(f"{word} is a palindrome.")
# else:
#     print(f"{word} is not a palindrome.")
