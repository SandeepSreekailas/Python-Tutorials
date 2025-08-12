# def recursion(n):
#     if n<=1:    
#      return n
#     else:
#        return n  * recursion(n-1)
    
# s=recursion(5)
# print(s)


# def f(n):
#         if n == 0 or n == 1:
#             return 1

#         else:
#             return n * f(n - 1)

# print(f(5))  

# def iterative_factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i 
#     return result
# print(iterative_factorial(5))


# def tail_factorial(n, accumulator=1):
#     if n == 0 or n == 1:
#         return accumulator
#     else:
#         return tail_factorial(n - 1, accumulator * n)

# print(tail_factorial(5))  



# def fibonacci(n):
#     # Base cases
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     # Recursive case
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(9))  


def sum_list(lst):
    # Base case
    if not lst:
        return 0
    # Recursive case
    else:
        return lst[0] + sum_list(lst[1:])
print(sum_list([1, 2, 3, 4, 5]))  


# def iterative_factorial(n): 
#     result = 1 
#     for i in range(1, n + 1): 
#         result *= i 
#     return result 
# print(iterative_factorial(5))