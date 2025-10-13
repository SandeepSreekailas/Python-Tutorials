# 1.Right-angled triangle

# n = 5
# for i in range(1, n+1):
#     print("*" * i)


# 2. Inverted right-angled triangle

# n = 5
# for i in range(n, 0, -1):
#     print("*" * i)


# 3. Pyramid pattern

# n = 5
# for i in range(1, n+1):
#     print(" " * (n-i) + "*" * (2*i-1))


# 4.Diamond pattern

# n = 5
# for i in range(1, n+1):
#     print(" " * (n-i) + "*" * (2*i-1))
# for i in range(n-1, 0, -1):
#     print(" " * (n-i) + "*" * (2*i-1))


# 5. Hollow square

# n = 5
# for i in range(n):
#     if i == 0 or i == n-1:
#         print("*" * n)
#     else:
#         print("*" + " " * (n-2) + "*")


# 6. Hollow pyramid

# n = 5
# for i in range(1, n+1):
#     if i == 5:
#         print("*" * (2*i-1))
#     elif i == 1:
#         print(" " * (n-1) + "*")
#     else:
#         print(" " * (n-i) + "*" + " " * (2*i-3) + "*")


#7 Hollow diamond

# n = 5
# for i in range(1, n+1):
#     if i == 1:
#         print(" " * (n-1) + "*")
#     else:
#         print(" " * (n-i) + "*" + " " * (2*i-3) + "*")
# for i in range(n-1, 0, -1):
#     if i == 1:
#         print(" " * (n-1) + "*")
#     else:
#         print(" " * (n-i) + "*" + " " * (2*i-3) + "*")

#8 Sandglass / Hourglass pattern

# n = 5
# for i in range(n, 0, -1):
#     print(" " * (n-i) + "*" * (2*i-1))
# for i in range(2, n+1):
#     print(" " * (n-i) + "*" * (2*i-1))

#9. Right-angled triangle (hollow)

# n = 5
# for i in range(1, n+1):
#     if i == 1 or i == n:
#         print("*" * i)
#     else:
#         print("*" + " " * (i-2) + "*")

# 10. S

# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or i+j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = 5
# for i in range(n):                 # rows
#     for j in range(n):             # columns
#         if (j == 0 or j == n-1     # left & right border
#             or i == j              # main diagonal ↘
#             or i + j == n-1):      # other diagonal ↙
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()