# Read an integer:
a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
b = (a%10)
c = ((a//10)%10)
d = ((a//100)%100)
print(b + c + d)