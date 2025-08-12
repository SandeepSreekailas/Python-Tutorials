# def message():
#     print("hello world")
# message()

# def message(a):
#     print(f"hello {a+1}: HOW ARE YOU" )

# for x in range(10):
#     message(x)    

# def find_sum(num1, num2):
#     print(num1+num2)

# find_sum(10,20)


# def finde_sum():
#     return 10 + 20

# print(finde_sum())

# def finde_sum(num):
#     return num + num

# print(finde_sum(10))

# Recursion
# def recursion(n):
#     if n<=1:    
#      return n
#     else:
#        return n + recursion(n-1)
    
# s=recursion(7)
# print(s)

#lambda function

# l = lambda x: x*x
# print(l(5))


# list1=[1,2,3,4,5,6,7,8,9,10]
# def even(x):
#     if x % 2==0:
#         return x
# f=filter(even,list1)
# print(list(f))

# list1=[1,2,3,4,5,6,7,8,9,10]
# f= filter(lambda x : x%2 == 0, list1)
# print(list(f))



# def hai(*values):
#     print('first:' + values[0], 'second:' + values[1], 'third:' + values[2])
# hai('messi', 'barcelona', 'Agrentina')

# def hai(**info):
#     print("first: " + info["first"])
#     print("second: " + info["second"])
#     print("third: " + info["third"])
    

# hai(first="messi",third="king", second="barcelona")  

# def hai(*values):
#     print(values)

# hai('messi', 'barcelona', 'Argentina')


# x = 10  

# def outer_function():
#     x = 5  
#     def inner_function():
#         x = 2  
#         print(x)
    
#     inner_function()

# outer_function()  # Output: 2
# print(x)  


# def palin(s):
#     s = s.replace(" ", "").lower()  
#     left, right = 0, len(s) - 1

#     while left < right:
#         if s[left] != s[right]:
#             return False  
#         left += 1
#         right -= 1

#     return True  

# String = input("Enter a string: ")

# if not String:
#     print("No string entered")  
# elif palin(String):
#     print("Entered string is a palindrome")
# else:
#     print("Entered string is not a palindrome")


# def pali(n):
#     s=str(n)
#     left,right=0, len(s)-1
#     while left<right:
#          if s[left]!=s[right]:
#              return False
#          left += 1
#          right -= 1
#          return True

# n=12578
# if pali(n):
#     print("Yes")
# else:
#     print("No")