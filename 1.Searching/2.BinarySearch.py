# Linear Search

def binarySearch(li, ele):
    start = 0
    end = len(li) - 1
    
    while(start <= end):
        mid = (start + end) // 2
        if(ele > li[mid]):
            start = mid + 1
        elif(li[mid] == ele):
            return mid
        else:
            end = mid - 1
        mid = (start + end) // 2
    return -1
        



print("Enter the size of an array")
size = int(input())
print("Enter the elements in an array(space sparated)")
li = [int(n) for n in input().split()]

print("Enter the element which you want to search")
ele = int(input())

index = binarySearch(li, ele)
print(index)


