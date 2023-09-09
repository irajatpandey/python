class DynamicArray:
    arr = []
    capacity = 0
    def __init__(self, capacity):
        self.capacity = capacity
        
    # Get the size of a Dyanamic Array
    def getSize(self):
        return len(DynamicArray.arr)
    
    # check the capacity of the dynamic array
    def getCapacity(self):
        return self.capacity
    
    # check array is empty or not
    def isEmpty(self):
        if(self.getCapacity() == 0):
            return True
        else:
            return False
        
    # Insert at the end
    def insert(self, item):
        if self.capacity == len(DynamicArray.arr):
           self.capacity *= 2
           tempArr = []
           for ele in DynamicArray.arr:
               tempArr.append(ele)
           arr = tempArr 
           del tempArr
        DynamicArray.arr.append(item)
    
    # Remove element from the last
    def removeFromLast(self):
        tempArr = []
        if self.isEmpty() == True:
            print("Array is empty")
            return
        self.capacity -= 1
        for i in range(len(DynamicArray.arr) - 1):
            tempArr.append(DynamicArray.arr[i])
        DynamicArray.arr = tempArr
        del tempArr
    
    # Remove Element from the Front
    def removeFromFront(self):
        tempArr = []
        if self.isEmpty() == True:
            print("Array is empty")
            return
        elif self.getSize() == 1:
            self.removeFromLast()
            return
        else:
            tempArr = []
            for i in range(1, len(DynamicArray.arr)):
                tempArr.append(DynamicArray.arr[i])
                DynamicArray.arr = tempArr
                del tempArr

arr = DynamicArray(2)
print(arr.getSize())
arr.insert(10)
arr.insert(20)
arr.insert(30)
print(arr.getSize())

print(DynamicArray.arr)
arr.removeFromLast()
print(DynamicArray.arr)

arr.removeFromFront()
print(DynamicArray.arr)
arr.removeFromFront()
print(DynamicArray.arr)
arr.removeFromFront()
print(DynamicArray.arr)




        