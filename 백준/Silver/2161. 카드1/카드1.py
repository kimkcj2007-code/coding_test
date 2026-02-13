# 백준 2161번 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cnt = 0

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            current = new_node
            self.tail.next = current
            self.tail = current

        self.cnt += 1

    def empty(self):
        return self.head is None

    def pop(self):
        if self.empty():
            self.tail = None
            self.cnt = 0
            return -1
            
        current = self.head
        self.head = current.next
        self.cnt -= 1
        return current.data

    def size(self):
        return self.cnt

    def front(self):
        return -1 if self.empty() else self.head.data
    def back(self):
        return -1 if self.empty() else self.tail.data


N = int(input())
q = Queue()
for i in range(1, N + 1):
    q.push(i)

while True:
    if q.size() == 1:
        break
    print(q.pop(), end=" ")

    if q.size() == 1:
        break

    q.push(q.pop())

print(q.pop())