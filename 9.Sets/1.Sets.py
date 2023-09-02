# Sets

set_1 = {"apple", 123, "abc"}
print(type(set_1))

# There is no order in sets so we cannot access element via
# index

#Loop

for ele in set_1:
    print(ele, end=" ")

# check ele is in set
print("apple" in set_1)

# Insertion
set_1.add("BMW") 
print(set_1) # {'abc', 123, 'apple', 'BMW'}

# Deletion
#remove - it will remove an element if present, else error
set_1.remove("apple")
print(set_1) # {123, 'abc', 'BMW'}
print(set_1.remove("rrr")) # error rrr is not present

#discard - it will remove an element if present, if not no error.
print(set_1.discard("rrr")) # None
