class Node:
        def __init__(self,data):
                self.data=data
                self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)

n1.next=n2
n2.next=n3
n3.next=n4

head=n1

print("MY Linked List")

def LinkedList(head):
        curr=head
        while(curr!=None):
                print(curr.data,end=" ")
                curr=curr.next 
LinkedList(head)

print("\nInsert new Node At last Position ")

newNode=Node(1)
curr=head
while curr.next!=None:
        curr=curr.next
curr.next=newNode
LinkedList(head)
        