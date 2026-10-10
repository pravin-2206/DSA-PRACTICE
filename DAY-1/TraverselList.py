class Node:
        def __init__(self,data):
                self.data=data
                self.next=None
n1=Node(100)
n2=Node(200)
n3=Node(300)

n1.next=n2
n2.next=n3

head=n1

curr=head
print("Traversel List:")
while curr.next!=None:
        print(curr.data,end=" ")
        curr=curr.next



                
                
        