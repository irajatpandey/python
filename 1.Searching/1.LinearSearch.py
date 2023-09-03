# Linear Search

def linearSearch(li, ele):
    for i in range(len(li)):
        if(li[i] == ele):
            return i
    return -1




print("Enter the size of an array")
size = int(input())
print("Enter the elements in an array(space sparated)")
li = [int(n) for n in input().split()]

print("Enter the element which you want to search")
ele = int(input())

index = linearSearch(li, ele)
print(index)


