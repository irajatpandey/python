# Iterating on Strings
str = "Hello World"
# count the frequency of l
count = 0
for letter in str:
    if letter == 'l':
        count += 1
print(count) # output - 3


# using index
count = 0
for i in range(len(str)):
    if str[i] == 'l':
        count += 1
print(count) # output - 3