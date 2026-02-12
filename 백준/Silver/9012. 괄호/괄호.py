class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.top = new_node
        else:
            current = new_node
            current.next = self.top
            self.top = current

    def display(self):
        if self.is_empty():
            return

        current = self.top

        while current:
            print(f"|  {current.data}  |")
            current = current.next

        print("--------")

    def peek(self):
        if self.is_empty():
            return None

        return self.top.data

    def pop(self):
        if self.is_empty():
            return None

        current = self.top
        self.top = self.top.next
        return current.data

def is_check(test):
    vps = Stack()
    is_valid = True
    for ps in test:
        if ps == "(":
            vps.push(ps)
        else:
            if vps.pop() == "(":
                continue
            else:
                is_valid = False
                break
    if not vps.is_empty():
        is_valid = False
    
    if is_valid:
        print("YES")
    else:
        print("NO")

T = int(input())
for _ in range(T):
    test = input()
    is_check(test)