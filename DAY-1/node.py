class Node:
        def __init__(self,data):
                self.data=data
                self.next=None
        
a=Node(10)  # create a object of node
b=Node(20)
c=Node(30) 

a.next=b
b.next=c

head=a

# print the list 
# print(head.data)
# print(head.next.data)
# print(head.next.next.data)

# traverse list  


def printLinkedList(head):
        curr=head
        while curr!=None:
                print(curr.data,end=" ") 
                curr=curr.next
printLinkedList(head)



# insert at beginning Node 

newNode=Node(12)

newNode.next=head
head=newNode

printLinkedList(head)


