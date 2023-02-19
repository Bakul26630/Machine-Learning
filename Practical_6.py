# Perform basic operations on matrices (like addition, subtraction, multiplication) and display
# specific rows or columns of the matrix.

def Add_Matrix(m1,m2):
    if(len(m1)==len(m2) and len(m1[0])==len(m2[0])):
        result=[]
        for i in range(0,len(m1)):
            temp=[]
            for index in range(0,len(m1[0])):
                temp.append(m1[i][index]+m2[i][index])
            result.append(temp)
        return result
    return []

def Subtract_Matrix(m1,m2):
    if(len(m1)==len(m2) and len(m1[0])==len(m2[0])):
        result=[]
        for i in range(0,len(m1)):
            temp=[]
            for index in range(0,len(m1[0])):
                temp.append(m1[i][index]-m2[i][index])
            result.append(temp)
        return result
    return []

def Multiply_Matrix(m1,m2):
    if len(m1[0])==len(m2):
        result=[]
        for i in range(0,len(m1)):
            temp=[]
            for j in range(0,len(m2[0])):
                val=0
                for k in range(0,len(m2[0])):
                    val+=(m1[i][k]*m2[k][j]) 
                temp.append(val)
            result.append(temp)

        return result
    else:
        return -1

matrix1=[[1,2,3],[4,5,6],[7,6,5]]
matrix2=[[1,2,3],[4,5,6],[1,1,1]]

print(Add_Matrix(matrix1,matrix2))
print(Subtract_Matrix(matrix1,matrix2))
print(Multiply_Matrix(matrix1,matrix2))