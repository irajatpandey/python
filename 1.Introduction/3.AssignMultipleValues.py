# Many Values to Multiple Variables
a, b, c = 1, 2, 3
print(a, " ", b, " ", c)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x, " ", y, " ", z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


m = 1
n = 2

print(id(m))
print(id(n))

m = 2

print()
print(id(m))
print(id(n))
