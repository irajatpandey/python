

a = 10
b = 20

if(id(a) == id(b)):
    print("pointing to same object\n")
else:
    print("pointing to different object\n")
    
# output pointing to different object
b = a
if(id(a) == id(b)):
    print("pointing to same object")
else:
    print("pointing to different object") 
    
# output pointing to same object