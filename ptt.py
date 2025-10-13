#Square Pattern

# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()


# triangle

# n=5
# for i in range (n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# reverse
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print ("*", end=" ")
#     print()


# n=5
# for i in range(n):
#     for j in range(i,n-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")  
#     print()


# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i,n):
#         print("*",end=" ")       
#     print()

#Pyramid

# n=5
# for i in range(n):
#     for j in range(i,n-1):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# Reverse Pyramid

# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i, n-1):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(n-1):
#     for j in range(i,n-1):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()


#hollow square
# n=5
# for i in range(n):
#     if i==0 or i==n-1:
#         print("*" * n)
#     else:
#         print("*" + " " * (n-2) + "*")


# hollow triangle
# n=5
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==i or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# hollow pyramid
# n=5
# for i in range(1,n+1):
#     if i==n:
#         print("* " * (2*i-n))
#     elif i==1:
#         print(" "*(n-i)+"*")
#     else:
#         print(" "*(n-i)+"*"+ " "*(2*i-3)+"*")


# n=5
# for i in range(n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
        