# Creation of List
li = [10, 20, "apple", 3.14] #created
print(li)

# accessing list's element via indexing
print(li[1]) # output - 2

#print(li[9]) # will give an error out of range.

# Slicing of Lists

print(li[1:3])  #output - [20, 'apple']
print(li[1:10]) #output - [20, 'apple', 3.14]
print(li[:]) #output - [10, 20, "apple", 3.14]

# Insert and Append element in a list
li.append("India") # a new element gets added at last
print(li) # output - [10, 20, 'apple', 3.14, 'India']

#Insert
#li.insert(index, value)
li.insert(1, 41)
print(li) # output - [10, 41, 20, 'apple', 3.14, 'India']

li.insert(100, "py") # if len(li) < index given, it will insert element at last.
print(li)

# Extend
# If we want to insert multiple element in one short we can use extend

li.extend(["New Jersey", "Berlin", "Prague"])
print(li) # output - [10, 41, 20, 'apple', 3.14, 'India', 'py', 'New Jersey', 'Berlin', 'Prague']