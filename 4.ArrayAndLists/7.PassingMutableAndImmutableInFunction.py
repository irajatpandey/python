#immutable
def increment(a):
    a += 2
    print(id(a))
    return a


a = 2
print(id(a))
a = increment(a)
print(a)

# mutable
def incrementInList(li):
    for i in range(len(li)):
        li[i] += 1

li = [1, 2, 3]
incrementInList(li)
print(li)
    