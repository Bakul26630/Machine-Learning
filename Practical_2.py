# Perform elementary logical operations in Octave/MATLAB (like OR, AND, Checking for Equality, NOT, XOR).
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

andOp = a and b
orOp = a or b
equalityOp = a==b
notEqualityOp = a!=b
xorOp = a^b
notaOp = not a
notbOp = not b

print(f"a and b: {andOp}")
print(f"a or b: {orOp}")
print(f"a==b: {equalityOp}")
print(f"a!=b: {notEqualityOp}")
print(f"a^b: {xorOp}")
print(f"not a: {notaOp}")
print(f"not b: {notbOp}")