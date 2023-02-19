# Use command to compute the size of a matrix, size/length of a particular row/column, load 
# data from a text file, store matrix data to a text file, finding out variables and their features in the
# current scope.

def check_Matrix(matrix):
    isMatrix = True
    rowLen = len(matrix[0])
    for i in matrix:
        if len(i)!=rowLen:
            isMatrix=False

    return isMatrix

# Computing the size of a matrix
def matrix_size(matrix):
    if(check_Matrix(matrix)):
        return (len(matrix),len(matrix[0]))
    else:
        return (-1,-1)

# Computing size of a row of a matrix
def rowLength(matrix,rowNum):
    if check_Matrix(matrix) and rowNum<=len(matrix):
        return len(matrix[rowNum-1])
    else:
        return -1
    
# Computing the size of a column of a matrix
def columnLength(matrix,colNum):
    if(check_Matrix(matrix) and colNum<=len(matrix[0])):
        return len(matrix)
    else:
        return -1
matrix1 = [
    [10,2,0,6,5,7],
    [6,4,8,7,6,12],
    [7,8,9,1,2,3],
    [0,0,1,2,3,12]
]

print(matrix_size(matrix1))
print(rowLength(matrix1,4))
print(columnLength(matrix1,5))
print(check_Matrix(matrix1))

# Reading data from a text file
data = open("./P5_1.txt",'r')
for i in data:
    print(i,end="")

# storing matrix data to a text file
employeeMatrix = [
    ["1","Rajveer","Senior Developer","80,000"],
    ["2","Samay","Developer","50,000"],
    ["3","Kamal","Manager","60,000"],
    ["4","Sonia","Hr","70,000"],
    ["5","Shivalik","CEO","5,00,000"]
]

writer = open("./P5_2.txt",'w+')
for i in employeeMatrix:
    temp=""
    for j in i:
        temp+=j
        temp+=" "
    temp+="\n"
    writer.write(temp)

