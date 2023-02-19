# Perform other matrix operations like converting matrix data to absolute values, taking the
# negative of matrix values, additing/removing rows/columns from a matrix, finding the maximum 
# or minimum values in a matrix or in a row/column, and finding the sum of some/all
# elements in a matrix.

import numpy as np

# Fuction for taking input matrix
def inputMatrix(m,n):
    matrix = []
    for i in range(0,m):
        temp=[]
        s = input(f"Enter {i+1} row: ")
        temp = [int(i) for i in s.split(" ")]
        matrix.append(temp)
    return matrix

# Function for converting matrix to absolute value matrix
def matrix_to_absMatrix(matrix):
    absMatrix = np.absolute(matrix)
    return absMatrix

# Function for converting matrix values to negative values matrix
def matrix_to_negativeMatrix(matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            matrix[i][j ] = (-1)*matrix[i][j]
    return matrix

# Function for adding rows to matrix
def addRow(matrix):
    print(f"Row Size-{len(matrix[0])}")
    temp = [int(i) for i in input("Enter Row to add to the matrix: ").split(" ")]
    matrix.append(temp)
    return matrix

# Function for adding columns to matrix
def addColumn(matrix):
    print(f"Column Size-{len(matrix)}")
    temp = [int(i) for i in input("Enter Column to add to the matrix: ").split(" ")]
    for i in range(0,len(matrix)):
        matrix[i].append(temp[i])
    return matrix

# Functions for removing row from a matrix
def removeRow(matrix,row_number):
    if((row_number-1) <= len(matrix)):
        del matrix[row_number-1]
    return matrix
        
# Functions for removing column from a matrix
def removeColumn(matrix,column_number):
    if((column_number-1)<=len(matrix[0])):
        for i in range(0,len(matrix)):
            del matrix[i][column_number-1]
    return matrix

# Function for determining maximum and minimum value of a matrix
def max_min_matrix(matrix):
    max=(-2)**31 -1
    min = 2**32

    for i in matrix:
        for j in i:
            if j>max:
                max=j
            if j<min:
                min=j
    return (max,min)

# Function for determining max and min of each row of matrix
def max_min_row(matrix):
    res=[]
    for i in matrix:
        max=(-2)**31 -1
        min = 2**32
        for j in i:
            if j>max:
                max=j
            if j<min:
                min=j
        res.append((max,min))
    return res

# Function for determining max and min of each column of matrix
def max_min_column(matrix):
    res=[]
    for i in range(0,len(matrix[0])):
        max=(-2)**31 -1
        min = 2**32
        for j in range(0,len(matrix)):
            if matrix[j][i]>max:
                max=matrix[j][i]
            if matrix[j][i]<min:
                min=matrix[j][i]
        res.append((max,min))
    return res
def sum_matrix(matrix):
    res=[]
    temp=[]
    for i in matrix:
        sum=0
        for j in i:
            sum+=j
        temp.append(sum)
    res.append({"Rows":temp});

    temp=[]
    for i in range(0,len(matrix[0])):
        sum=0
        for j in range(0,len(matrix)):
           sum+=matrix[j][i]
        temp.append(sum)
    res.append({"Columns":temp});
    
    sum=0
    for i in temp:
        sum+=i
    res.append({"Matrix":sum})
    return res

m=int(input("Enter number of rows: "))
n=int(input("Enter number of columns: "))

matrix = inputMatrix(m,n)
negativeMatrix = matrix_to_negativeMatrix(matrix)
print(negativeMatrix)
matrix = addRow(matrix)
print(matrix)
matrix = addColumn(matrix)
print(matrix)

removeRowNumber = int(input("Enter Row number to remove: "))
matrix=removeRow(matrix,removeRowNumber)
print(matrix)

removeColumnNumber = int(input("Enter Column number to remove: "))
matrix=removeColumn(matrix,removeColumnNumber)
print(matrix)

print(max_min_matrix(matrix))
print(max_min_row(matrix))
print(max_min_column(matrix))
print(sum_matrix(matrix))