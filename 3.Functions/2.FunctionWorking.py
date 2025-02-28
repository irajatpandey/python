def A():
    B()
    print("A")
    
def B():
    C()
    print("B")
       
def C():
    print("C")
    
A()