class Node:
  

    def __init__(self, data):
        self.data = data  
        self.next = None  
                         
  

class LinkedList:
    
   
    
    def __init__(self):
        self.head = None
    
    def append(self, new_data):
 
        new_node = Node(new_data)
 
        if self.head is None:
            self.head = new_node
            return 
        last = self.head
        while (last.next==None):
            last = last.next
        last.next = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
    def revers(self):
        if self.head is None or self.head.next is None:
            return self.head 

        else:
            first=self.head
            last=self.head
            while(last.next==None):
                

list=LinkedList()
list.append(141)
list.append(142)
list.append(143)
list.printList()