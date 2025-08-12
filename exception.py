# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("Division by zero is not allowed!")
# else:
#     print(f"The result is {result}")

# finally:
#     print("This will always be printed.")


# x = -5
# if x < 0:
#     raise ValueError("Negative numbers are not allowed!")


class NegativeNumberError(Exception):
    pass

def check_number(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")


print(check_number(-10))

   



# print(5 + "hello")  #type error

# int("abc") #value error

# my_list = [1, 2, 3]
# print(my_list[5])  #index error

# my_dict = {"name": "Alice", "age": 25}
# print(my_dict["gender"])  #key error


