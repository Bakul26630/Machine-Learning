# Create/Define single dimension / multi-dimension arrays, and arrays with specific values like array of all ones, 
# all zeros, array with random values within a range, or a diagonal matrix.
import numpy as np

# Creating and Defining Single Dimensional Array by taking input from user
s = input("Enter list elements: ")
l = [int(x) for x in s.split(" ")]

a1  = np.array(l)
print(a1)

# Creating and Defining Single Dimensional Array of random values
a2 = np.random.rand(20)*100
print(a2)

# Creating and Defining Single Dimensional Array of random integer values
a3 = np.random.randint(10,200,15)
print(a3)

# Creating and Defining Multi Dimensional Array of random values
a4 = np.random.rand(10,20)*100
print(a4)

# Creating and Defining Multi Dimensional Array of random integer values
a5 = np.random.randint(10,200,(10,30))
print(a5)

# Single Dimensional Array of all ones
a6 = np.ones(20,dtype="int")
print(a6)

# Multi Dimensional Array of all ones
a7 = np.ones((15,27),dtype="int")
print(a7)

# Single Dimensional Array of all zeros
a8 = np.zeros(20,dtype="int")
print(a8)

# Multi Dimensional Array of all zeros
a9 = np.zeros((15,27),dtype="int")
print(a9)

# Diagonal Matrix with same element at diagonal
a10 = np.eye(10,dtype="int")*20
print(a10)