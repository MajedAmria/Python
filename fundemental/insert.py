class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

   

    def insert_index(self,index,data):
        node=Node(data)
        if self.head is None and index!=0:
            self.head=node
            return
        if self.head is not None and index==0:
            node.next=self.head
            self.head=node
            return 
        curr=self.head
        counter=0
        while curr is not None:
            counter+=1
            curr=curr.next
            if counter==index:
                node.next=curr
                curr.next=node.next
                return

    def print(self):
        temp=self.head
        while temp is not None:
            print (temp.data)
            temp = temp.next 
list=LinkedList()

list.insert_index(2,10)


list.print()





        

       
       

# first should make a class node
#make a linked list class
#declar a method insert_index have two parametar index and data
#inside method creat object of node
# and check liked list is empty and index not equal zero
#and check liked list is not empty and index equal zero
# make curr pointer equal head
#and make pointer prev equal none
