# Read an integer:
a = int(input())
b = int(input())
c = int(input())
# b = float(input())
# Print a value:
# print(a, b)

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else: 
    print(0)