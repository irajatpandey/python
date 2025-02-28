n = 37
if(n % 2 == 0):
    print("Even")
else:
    print("Odd")
    
# using bitwise operator
if(not(n & 1)):
    print("Even")
else:
    print("Odd")
    

if((n ^ 1) == (n + 1)):
    print("Even")
else:
    print("Odd")