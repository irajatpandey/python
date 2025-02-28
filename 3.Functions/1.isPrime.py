def isPrime(n):
    for i in range(2, n):
        if(n % i == 0):
            break
    else:
        return True
    return False

print(isPrime(17)) # True