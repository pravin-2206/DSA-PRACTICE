class Node:
        def __init__(self,data):
                self.data=data
                self.next=None
obj1=Node(5)
obj2=Node(6)
obj3=Node(7)


obj1.next=obj2
obj2.next=obj3

head=obj1

print("Given List:")
def TraverselList(head): 
        curr=head       
        while curr!=None:
                print(curr.data,end=" ")
                curr=curr.next
TraverselList(head)
        
print("\nInsert New Node at first Position:")

newNode =Node(20)
newNode.next=head
head=newNode
# print(head.data)
TraverselList(head)