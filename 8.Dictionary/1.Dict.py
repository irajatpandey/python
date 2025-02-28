a = {}
print(type(a))
a = {"apple" : 5, "grapes" : 10}
print(a)

a = {1 : 2, 3 : 4, "list": [10, 20, 30], "dict" : {"Code" : "Python"}}

print(a.keys()) # print all the keys in dictionary
print(a.get(1)) #print value associated with key 1
print(a.get("my_key")) # output - None
print(a.get("my_key", 0)) # will return 0 if key is not present output - 0

#Loop
for key in a.keys():
    print(a.get(key))
    
# Check key is present or not    
if "test" in a:
    print("True")
else: 
    print("False")
    
# Add two dictionaries

d1 = {"brand": "Ford", "model": "Mustang", "year": 1964}
d2 = {"United States": "Washington D.C.", "Italy": "Rome", "England": "London"}

d1.update(d2) 
print(d1)

# Insertion

d2["India"] = "New Delhi" # added

# Deletion
d2.pop("United States")

print(d2)
