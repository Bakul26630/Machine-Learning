#  Use conditional statements and different type of loops based on simple example/s.
import random
import math
# using if-elif-else ladder
def Calc1(exp):
    if '+' in exp:
        ind = exp.find('+')
        first = exp[0:ind]
        second=exp[ind+1:]
        return int(first)+int(second)
    elif '-' in exp:
        ind = exp.find('-')
        first = exp[0:ind]
        second=exp[ind+1:]
        return int(first)-int(second)
    elif '*' in exp:
        ind = exp.find('*')
        first = exp[0:ind]
        second=exp[ind+1:]
        return int(first)*int(second)
    elif '/' in exp:
        ind = exp.find('/')
        first = exp[0:ind]
        second=exp[ind+1:]
        return int(first)/int(second)
    else:
        return 0;

# using switch case
def Calc2(a,b,op):
    switcher = {
        "+":a+b,
        "-":a-b,
        "*":a*b,
        "/":a/b
    }

    return switcher.get(op,0);

# exp = input("Enter Expression with two operands only: ")
# print(Calc1(exp))

print(Calc2(100,789,"+"))
print(Calc2(784,145,"-"))
print(Calc2(146,207,"*"))
print(Calc2(105,20,"/"))

# using for loop 
for i in range(1,21):
    print(f"15 X {i} = {15*i}")

# using for in loop
l = [math.trunc(random.random()*100) for i in range(0,20)]
for i in l:
    print(i,end=" ")
print()

# using while loop
ind = 0
while ind<len(l):
    print(l[ind],end=" ")
    ind+=1
print()