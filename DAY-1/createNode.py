class Node:
        def __init__(self,data):
                self.data=data
                self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)

n1.next=n2
n2.next=n3

head =n1

# print(head.data)
# print(head.next.data)
# print(head.next.next.data)

def Traversal(head):
        curr=head
        while curr!=None:
                print(curr.data,end=" ")
                curr=curr.next 
Traversal(head)
print()
# insert at beginning 
newnode=Node(5)
newnode.next=head
head=newnode

print(Traversal(head))
newnode=Node(1)
curr=head # Starts traversal from the first node.

while curr.next!=None:  # check whether the current node is last node
        curr=curr.next # move to the next node

curr.next=newnode  # connect last node with newnode
print(Traversal(head)) 
