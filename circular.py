
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.rear is None:
            self.front = self.rear = new_node
            new_node.next = new_node
        else:
            new_node.next = self.front
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front

        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

        temp.next = None

    def print(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front

        while True:
            print(temp.data, end="  ")
            temp = temp.next

            if temp == self.front:
                break

        print()


q = Queue()

q.enqueue(Node(15))
q.enqueue(Node(25))
q.enqueue(Node(30))
q.enqueue(Node(45))
q.enqueue(Node(40))

print("Circular Queue elements:")
q.print()

q.dequeue()
q.dequeue()

print("After removing two elements:")
q.print()

q.dequeue()
q.dequeue()
q.dequeue()

print("After removing all elements:")
q.print()
