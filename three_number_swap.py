x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Before swapping: x =", x, ", y =", y, ", z =", z)

x, y, z = y, z, x

print("After swapping: x =", x, ", y =", y, ", z =", z)
