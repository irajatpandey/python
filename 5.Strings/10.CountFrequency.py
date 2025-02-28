# Count Vovels Cononants Digits and Special Characters

str = "abc123$PQR,ajeilonu!!"
print(len(str))
v, c, d, s = 0, 0, 0, 0

for item in str:
    #print(item)
    if(item >= 'a' and item <= 'z') or (item >='A' and item <= 'Z'):
        item = item.lower()
        if(item == 'a' or item == 'e' or item == 'i' or item == 'o' or item == 'u'):
            v += 1
        else:
            c += 1
    elif(item >= '0' and item <= '9'):
        d += 1
    else:
        s += 1


print(v)
print(c)
print(d)
print(s)
        