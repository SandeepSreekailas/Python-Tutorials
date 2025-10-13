import numpy as np

# a=np.array([[1,2,3,4]
#     ,[5,6,7,8]
#     ,[9,10,11,12]])
# b=a.reshape(-1)
# print(b.shape)


# a=np.array([[1,2,3,4]
#     ,[5,6,7,8]
#     ,[9,10,11,12]])
# print(a.dtype)

# b=np.array([1,2,3,4])
# print(b.dtype)

# d=np.array(['a','b','c'])
# print(d.dtype)

# c=np.array([1,2,3,4],dtype=np.float64)
# print(c.dtype)
# print(c)

# e=np.array([1.1,2.2,3.3,4.4],dtype=np.int32)
# print(e.dtype)
# print(e)

# f=np.array([1,2,3,4],dtype=np.int32)
# g=f.astype(np.float64)
# print(g.dtype)
# print(g)

# f=np.array([1,2,3,4],dtype=np.int32)
# g=f.astype(np.uint16)
# print(g.dtype)
# print(g)

##########################################################

# Array creatin method

#1) numpy.array

# list1=[1,2,3,4]
# a=np.array(list1)
# print(a)

# 2) numpy.zeros:- it creates an array of zeros


# a=np.zeros(5)
# print(a)

# 3) numpy.ones:- it creates an array of ones

# a=np.ones(5)
# print(a)

# 4) numpy.arange:- it creates an array of evenly spaced values just like range in for loop

# a=np.arange(10)
# print(a)

# a=np.arange(0,10,2)
# print(a)

# 5) numpy.linspace:- function that creates a NumPy array of a specified number of evenly spaced values between a start and stop, including the end by default.

# a=np.linspace(0,10)
# print(a) # by default 50


# 6) numpy.eye:- function that creates a 2-D NumPy array with ones on the diagonal and zeros elsewhere.

# a=np.eye(3)
# print(a)

# a=np.eye(3,4,k=-1) # k is used to shift the diagonal 
# print(a)

# 7) numpy.full:- function that creates a NumPy array of a specified shape and type, filled with a constant value.

# a=np.full((3,4,3),5)
# print(a)

# 8) numpy.random.randint:- function that returns random integers from low (inclusive) to high (exclusive).

# a=np.random.randint(0,10,10)
# print(a)

# a=np.random.randint(0,10,(3,4))
# print(a)

# 9) numpy.random.random:- function that returns random floats in the half-open interval [0.0, 1.0).

# a=np.random.random((3,4,3))
# print(a)

############################################################################################

# Array indexing

# 1d array

# a=np.array([1,2,3,4])
# print(a[0])

# 2d array

# a=np.array([[1,2,3,4]
#     ,[5,6,7,8]
#     ,[9,10,11,12]])
# print(a[1,2])


# 3d array

# a=np.array([[[1,2,3,4]
#     ,[5,6,7,8]
#     ,[9,10,11,12]]
#     ,[[1,2,3,4]
#     ,[5,6,7,18]
#     ,[9,10,11,12]]])
# print(a[1,1,3])

#######################################################################

# Array slicing

# 1d array

# a=np.array([1,2,3,4])
# print(a[1:3])

# 2d array

# a=np.array([[1,2,3,4]
#     ,[5,6,7,8]
#     ,[9,10,11,12]])
# print(a[1:3,2:4])

# 3d array

# a=np.array([[[1,2,3,4]
#     ,[5,6,7,8]
#     ,[9,10,11,12]]
#     ,[[1,2,3,4]
#     ,[5,6,7,18]
#     ,[9,10,11,12]]])
# print(a[1,1:3,1:4])