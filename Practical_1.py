# Perform elementary mathematical operations in Octave/MATLAB like addition, multiplication, division and exponentiation.
# Addition
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

sum = a+b
mul = a*b
div1=a/b
div2=b/a
exp1=a**b
exp2=b**a

print(f"a+b={sum}")
print(f"a*b={mul}")
print(f"a/b={div1}")
print(f"b/a={div2}")
print(f"a**b={exp1}")
print(f"b**a={exp2}")