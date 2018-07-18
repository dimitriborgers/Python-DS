# R1
current = a._head
while current._next._next != None:
    current = current._next

# R2
Non-Coding
"""implement instead"""
def mergeLL(a,b,c = SinglyLinkedList()):
    curr = a._head
    while curr:
        c.append(curr._element)
        curr = curr._next
    curr = b._head
    while curr:
        c.append(curr._element)
        curr = curr._next
    return c

# R3
Non-Coding
"""implement instead"""
def countNodes(LLhead):
    if not LLhead._next:
        return 1
    else:
        return 1 + countNodes(LLhead._next)

# R4
def swapDLL(node1,node2):
    predecessor = node1._previous
    successor = node2._next
    predecessor._next = node2
    successor._previous = node1
    node1._next = successor
    node2._previous = predecessor
    node2._next = node1

# R5
def countNodes(CircularLL):
    current = current2 = CircularLL._head
    total = 1
    while current2._next != current:
        total += 1
        current2 = current2._next
    return total

# R6
"""implement instead"""
def check(x,y):
    while x._next != x:
        if x._next == y:
            return 'found'
        x._next = x._next._next
    return 'not found'

# R7
def rotate(LinkedQ):
    LinkedQ._tail._next = LinkedQ._head
    LinkedQ._head = LinkedQ._head._next
    LinkedQ._tail = LinkedQ._tail._next
    LInkedQ._tail._next = None

# R8
def middle(DLL):
    begin = DLL._header
    end = DLL._trailer
    while begin != end:
        if begin._next == end:
            return begin
        begin = begin._next
        end = end._next
    return begin

# R9
def mergeDLL(L,M):
    SLL = SinglyLinkedList()
    current = L._header._next
    while current != L._trailer:
        SLL.append(current)
        current = current._next
    while current != M._trailer:
        SLL.append(current)
        current = current._next
    return SLL

# R10
Non-Coding

# R11
def __max__(self):
    current = self._header._next
    currentMax = self._header_.next
    while current:
        current = current._next
        if currentMax < current:
            currentMax = current
    return currentMax

# R12
def max(self):
    current = self.first()
    max_ = current.element()
    while current:
        if current.element() > max_:
            max_ = current.element()
        current = self.after(current)

# R13
def find(self,e):
    current = self.first()
    while current:
        if current.element() == e:
            return current
        else:
            current = self.after(current)
    return None

# R14
def findRec(self,e):


# R15
def __reersed__(self):


# R16


# R17


# R18


# R19
Non-Coding

# R20


# R21


# R22


# R23


# C24
class LinkedStack:

    class _Node:
        __slots__ = '_element','_next'

        def __init__(self, _element, _next):
            self._element = _element
            self._next = _next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        outcome = []
        current = self._head
        while current:
            outcome.append(current._element)
            current = current._next
        return "{}".format(outcome)

    def is_empty(self):
        return self._size == 0

    def top(self):
        if self.is_empty():
            raise Exception('Stack is Empty')
        else:
            return self._head._element

    def add(self,e):
        self._head = self._Node(e,self._head)
        self._size += 1

    def pop(self):
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        return result

# C25
class LinkedQueue:

    class _Node:
        __slots__ = '_element','_next'

        def __init__(self, _element, _next):
            self._element = _element
            self._next = _next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        outcome = []
        current = self._head
        while current:
            outcome.append(current._element)
            current = current._next
        return "{}".format(outcome)

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception('Queue is Empty')
        else:
            return self._head._element

    def enqueue(self,e):
        if self.is_empty():
            self._tail = self._head = self._Node(e,None)
        else:
            self._tail._next = self._tail = self._Node(e,None)
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return Exception('Queue is Empty')
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return result

# C26


# C27


# C28


# C29


# C30


# C31


# C32


# C33


# C34


# C35


# C36


# C37


# C38


# C39


# C40


# C41


# C42


# C43


# P44


# P45


# P46


# P47

