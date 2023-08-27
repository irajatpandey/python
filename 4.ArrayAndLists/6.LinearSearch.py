# Linear Search

def linearSearch(li, item):
    for i in range(len(li)):
        if(item == li[i]):
            return i
    return -1
print("Size of an array")
n = int(input())
print("Please give space separated input")
li = [int(x) for x in input().split()]
print("Enter the element which you want to search!!")
ele = int(input())


print(linearSearch(li, ele))  # output -1 // means element does not exist