def total(a, b, *more):
    ans = a + b
    for i in more:
        ans += i
    return ans

print(total(10, 20, 50)) # can pass n number of variable

def calculation(a, b):
    return a + b, a - b

# single variable will hold the whole tuple
ans = calculation(5, 2)
print(ans) #output (7, 3)

# number of reciever should be equal to length of tuple
x, y = calculation(5, 2) 
print(x, y) #output 7 3