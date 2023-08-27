def calculateOverAllocatedMemory(size):
    allocated = size + (size >> 3) + (3 if size < 9 else 6)
    print(size, " -> ", allocated)

li = []
print(li.__sizeof__()) #40
calculateOverAllocatedMemory(len(li))

li.append(10)
print(li.__sizeof__()) # 40 + 8 + 8 + 8 + 8 = 72
calculateOverAllocatedMemory(len(li))

my_list = ["apple"]
print(my_list.__sizeof__()) # output 40 + 8 = 48
calculateOverAllocatedMemory(len(my_list))



