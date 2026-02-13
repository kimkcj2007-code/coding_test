class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

        
class Queue:
    def __init__(self):
        self.head = None # 머리부분
        self.tail = None # 꼬리부분
        self.cnt = 0 #size를 구현하기 위한 개수 정보 변수 # size기능의 두번째 방법

    # push X: 정수 X를 큐에 넣는 연산이다. 
    # push
    # 1)새로운 노드를 new_node
    # head와 tail이 해당 노드를 가리키게!!!
    def push(self, data):
        new_node = Node(data)

        if self.head is None: #헤드가 비어있다면
            self.head = new_node
            self.tail = new_node
        else: #헤드가 비어있지 않다면
            current = new_node # current를 새로운 노드 가리키게
            self.tail.next = current # 원래 꼬리 30의 next가 current(new node) 가리킨다
            self.tail = current # 이 테일을 뉴 노드로 교체
            # 10 -> 20 -> 30 -> None
            # 여기서 40 들어오기
            # 그러면 30이 40을 가리키게 해야 한다
            # 우리의 목표는, (원래) 테일의 넥스트가 40을 가리키게 하자
            # 그리고 이 테일을 40으로 바꾸자
        
            # 다른 방법
            #current = self.tail
            #current.next = new_node
            #self.tail = new_node
        self.cnt += 1

    def empty(self): # 큐가 비어있으면 1, 아니면 0 출력한다
        # 들어오는건 꼬리, 나가는건 헤드에서
        # 그러므로, 헤드에 없으면 아무것도 없는거다(비어있음)
        return self.head is None

    # pop
    # pop: # 큐에서 가장 앞에 있는 정수를 빼고 그 수를 출력한다.
    
    def pop(self):
        if self.empty():  # 비어있으면 -1 리턴
            self.tail = None
            self.cnt = 0
            return -1
            
        current = self.head # current 만들어서 헤드를 가리키게 
        self.head = current.next # (current.next = self.head.next)
        self.cnt -= 1
        return current.data

    def size(self):


         # 2) # 두번째 방법, 들어올 때마다, 뺄 때마다 cnt 를 증감시키고 그걸 리턴
        return self.cnt # 두번째 방법
        
        # 큐에 들어있는 정수 개수 반환!!
        # 비어있으면  - > 0
        # 우리에게 주어진 정보는 head, tail
        # head 부터 출발해서 node 개수 세기
    def front(self):
        #큐의 가장 앞에 있는 정수를 출력한다. 만약 들어있는거 없으면 -1 출력
        if self.empty():
            return -1
        else:
            return self.head.data
        
    def back(self):
        #큐의 가장 뒤에 있는 정수를 출력한다. 만약 들어있는거 없으면 -1 출력
        if self.empty():
            return -1
        else:
            return self.tail.data
N = int(input())
#N = 4 #일때 답은 4
# N = 6일 때 답은 4
# N = int(input())

cq1 = Queue()
for i in range(1, N+1, 1):
    cq1.push(i)

while True:
    if cq1.size() == 1:
        break
    else:
        cq1.pop()
        
    if (cq1.size() == 1):
        break
    else:
        cq1.push(cq1.pop())
print(cq1.pop())