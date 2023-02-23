# Perform vectorized implementation of simple matrix operation like finding the transpose of a
# matrix, adding, subtracting or multiplying two matrices.

import numpy as np
from time import time as t

m1 = np.random.randint(0,1000,size=(100,100))

# Transpose of a matrix
print("Original Matrix")
print(m1)
start=t()
m1=m1.transpose()
end=t()
print("Transposed Matrix")
print(m1)
print("Time Taken: ",end-start)

m1=np.random.randint(0,1000,size=(100,100))
print("First Matrix")
print(m1)

m2=np.random.randint(0,1000,size=(100,100))
print("Second Matrix")
print(m2)

# Addition of two matrices
print()
start=t()
sum=m1+m2
end=t()
print("Matrix1 + Matrix2")
print(sum)
print("Time Taken: ",end-start)

# Subtraction of two matrices
print()
start=t()
sub=m1-m2
end=t()
print("Matrix1 - Matrix2")
print(sum)
print("Time Taken: ",end-start)

# Multiplication of two matrices
print()
start=t()
sub=m1*m2
end=t()
print("Matrix1 x Matrix2")
print(sum)
print("Time Taken: ",end-start)
