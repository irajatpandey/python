# Split function

str = "I love Mangoes"
print(str.split()) # split function, splits the string
                   # on space delimeter and returns a list
# output - ['I', 'love', 'Mangoes']

# replace(oldvalue, newvalue, count)
# count - Optional. A number specifying how many occurrences of the old value you want to replace. 
# Default is all occurrences

str = str.replace("Mangoes", "Apple")
print(str) # I love Apple

# find() return a index of first occurence of a substring

str = "My name is John Wick and Mr. Hector and John Wick has rivalry"
index = str.find("Wick")
print(index) #output - 16 -[First wick]

# if you want to find the particular occurence of a substring pass index in find() function

index = str.find("Wick", 20, len(str))
print(index) #output - 45 [second Wick]