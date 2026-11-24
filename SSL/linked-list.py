class Node:
        def __init__(self,val):
                self.val=val
                self.next=None

class SingleLinkedList:
        def __init__(self):
                self.head=None
                
        def append(self,data):
                newNode=Node(data)
                if self.head is None:
                        self.head=newNode
                else:
                        curr=self.head
                        while curr.next is not None:
                                curr=curr.next
                        curr.next=newNode
        
        def Traverse(self):
                if self.head is None:
                        print("SSL is empty")
                else:
                        curr=self.head
                        while curr is not None:
                                print(curr.val, end=" ")
                                curr=curr.next
                        print()
                        
        def insert_at(self,val,pos):
                newNode=Node(val)
                if pos==0:
                        newNode.next=self.head
                        self.head=newNode
                else:
                        curr=self.head
                        prevNode=None
                        count=0
                        while curr is not None and count<pos:
                                prevNode=curr
                                curr=curr.next
                                count+=1
                        prevNode.next=newNode
                        newNode.next=curr
                        
        def delete(self,val):
                temp=self.head
                if temp.next is not None:
                        if temp.val==val:                                
                                self.head=temp.next
                                return
                        else:
                                prev=None
                                while temp is not None:
                                        if temp.val == val:
                                                prev.next = temp.next
                                                return
                                        prev=temp
                                        temp=temp.next
                                print("Value not found")
                        
sll=SingleLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(1)
sll.Traverse()
sll.insert_at(11,2)
sll.Traverse()
sll.delete(30)
sll.Traverse()
        