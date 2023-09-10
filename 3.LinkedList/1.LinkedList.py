class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
       
class LinkedList:
    __head = None
    def isEmpty(self):
        return self.__head == None
    
    def insertAtBegining(self,data):
        n1 = Node(data)
        n1.next = self.__head
        self.__head = n1
        return

    def printLinkeList(self):
        temp = self.__head
        while(temp != None):
            print(temp.data, end = " ")
            temp = temp.next
        print()
            
    def insertAtEnd(self,data):
        if self.isEmpty():
            n1 = Node(data)
            self.__head = n1
            return
        temp = self.__head
        while(temp.next != None):
            temp = temp.next
        n1 = Node(data) 
        temp.next = n1
        return   
    
    def deleteFirst(self):
        if self.isEmpty():
            print("List is Empty")
            return
        temp = self.__head
        self.__head = self.__head.next
        del temp
        
    def deleteLast(self):
        # List is empty
        if self.isEmpty():
            print("List is Empty")
            return
        
        # List has only 1 item
        elif self.__head.next == None:
            self.__head = None
            return
        
        # List is not empty
        temp = self.__head
        while(temp.next.next):
            temp = temp.next    
        temp.next = None
    
    def lengthOfLinkedList(self):
        length = 0
        temp = self.__head
        while(temp != None):
            length += 1
            temp = temp.next
        return length
    
    def insertAtPoisition(self, position, data):
        if(self.lengthOfLinkedList() < position):
            print("Out of Bound, please check the position!")
        else:
            if(position == 1):
                self.insertAtBegining(data)
            else:
                temp = self.__head
                for i in range(1, position - 1):
                    temp = temp.next
                n1 = Node(data)
                n1.next = temp.next
                temp.next = n1
                return
            
    def deleteAtPosition(self, position):
        if(self.lengthOfLinkedList() < position):
            print("Out of Bound, please check the position!")
        elif self.isEmpty() == True:
            print("List is empty")
            return    
        elif position == 1:
            self.deleteFirst()
            return
        else:
            temp = self.__head
            for i in range(1, position - 1):
                temp = temp.next      
            current = temp.next
            temp.next = current.next
            del current

l = LinkedList()
l.insertAtBegining(10)

l.insertAtBegining(20)
l.insertAtBegining(30)
l.insertAtBegining(40)
l.insertAtBegining(50)
l.printLinkeList() 

l.insertAtEnd(100)   
l.printLinkeList() 

l.deleteFirst()
l.printLinkeList() 

l.deleteLast()
l.printLinkeList()
l.deleteLast()
l.printLinkeList()


l.insertAtPoisition(4, 721)
l.printLinkeList()

l.deleteAtPosition(2)
l.printLinkeList()

