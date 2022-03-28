class Node:
  

    def __init__(self, data):
        self.data = data  
        self.next = None  
                         
  

class LinkedList:
    
   
    
    def __init__(self):
        self.head = None
    
    def append(self, new_data):
 
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

 
        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return self.head
 
        # 5. Else traverse till the last node
        last = self.head
        while (last.next==None):
            last = last.next
 
        # 6. Change the next of last node
        last.next = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next


list=LinkedList()
list.append(141)
list.append(142)
list.append(143)
list.printList()

