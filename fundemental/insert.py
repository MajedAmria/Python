class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def add(self, data):
 
        new_node = Node(data)
 
        if self.head is None:
            self.head = new_node
            return 
        last = self.head
        while (last.next!=None):
            last = last.next
        last.next = new_node


    def insert_index(self,index,data):
        node=Node(data)
        if self.head is None and index!=0:
            self.head=node
            
        if self.head is not None and index==0:
            node.next=self.head
            self.head=node
            
        curr=self.head
        prev=self.head
        counter=0
        while curr is not None:
            prev=curr
            curr=curr.next
            counter+=1
            if counter==index:
                node.next=curr
                curr=node.next
                prev.next=node
                
            
    def print(self):
        temp=self.head
        while temp is not None:
            print (temp.data)
            temp = temp.next 
list=LinkedList()
list.add(1)
list.add(2)
list.add(3)
list.add(4)
list.insert_index(0,10)


list.print()