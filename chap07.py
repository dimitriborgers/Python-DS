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
def findRec(self,e,start):
        if start.element() == e:
            return start
        else:
            return self.findRec(e,self.after(start))

# R15
def __reversed__(self):
    cursor = self.last()
    while cursor is not None:
        yield cursor.element()
        cursor = self.before(cursor)

# R16
Non-Coding

# R17
Non-Coding

# R18
Non-Coding

# R19
Non-Coding

# R20
Non-Coding

# R21
Non-Coding

# R22
def clear(self):
    self = PositionalList()
# R23
def reset_counts(self):
    cursor = self.first()
    while cursor:
        cursor.element()._count=0
        cursor = self.after(cursor)

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
def concatenate(self,other):
    self._tail._next = other._head
    other._head = other._tail = None

# C27
class LinkedListRecursive:

    class _Node:
        __slots__ = '_element','_next'

        def __init__(self,_element,_next):
            self._element = _element
            self._next = _next

    def __init__(self):
        self._head = None
        self._size = 0

    def append(self,e):
        if self._head == None:
            self._head = self._Node(e,LinkedListRecursive())
            self._size += 1
        else:
            self._head._next.append(e)
            self._size += 1

# C28
Non-Coding
"""implement instead"""
def revRec(self,curr):
    if curr._next._next == None:
        self._head = curr._next
        curr._next._next = curr
        return self
    else:
        self.revRec(curr._next)
        curr._next._next = curr
        curr._next = None
        self._tail = curr
    return self

# C29
Non-Coding
"""implement instead"""
def reverse(self):
    current = self._head
    cnext = current._next

    while current and cnext:
        new_c = cnext
        new_n = cnext._next

        cnext._next = current

        current = new_c
        cnext = new_n

    self._head._next = None
    self._head,self._tail = self._tail,self._head

# C30
class LeakyStack(SinglyLinkedQueue):

    def __init__(self,maxlen=10):
        super().__init__()
        self._maxlen = maxlen

    def enqueue(self,e):
        if self._size < self._maxlen:
            super().enqueue(e)
        else:
            self.dequeue()
            super().enqueue(e)

# C31
"""Same as C32"""

# C32
class PositionalCircular(CircularyLinkedQueue):

    class Position:
        def __init__(self,container,node):
            self._container = container
            self._node = node

        def __eq__(self,other):
            return self._container == other._container and self._node == other._node

    def enqueue(self,e):
        node = super().enqueue(e)
        return self.Position(self,node)

    def first(self):
        return self.Position(self,self._head)

    def after(self,p):
        return self.Position(self,p._node._next)

# C33
def reverse(self):
    current = self._header._next
    while current != self._trailer:
        next_ = current._next
        current._next,current._previous = current._previous,current._next
        current = next_
    self._trailer._next,self._trailer._previous = self._trailer._previous,self._trailer._next
    self._header._next,self._header._previous = self._header._previous,self._header._next
    self._header,self._trailer = self._trailer,self._header

# C34
def swap(self,p,q):
    p = self._validate(p)
    q = self._validate(q)
    p._next = q._next
    p._previous._next = q
    q._next._previous = p
    q._next = p
    q._previous = p._previous
    p._previous = q

# C35
class Iterator:

    def __init__(self,sequence):
        self._first = sequence._header
        self._last = sequence._trailer._previous

    def __next__(self):
        if self._first is self._last:
            raise StopIteration()
        else:
            self._first = self._first._next
            return self._first._element

def __iter__(self):
    return self.Iterator(self)

# C36
class PositionalList(_DoublyLinkedList):

    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not(self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self,node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self,node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._previous)

    def before(self,p):
        node = self._validate(p)
        return self._make_position(node._previous)

    def after(self,p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def __repr__(self):
        outcome = []
        current = self._header._next
        while current != self._trailer:
            outcome.append(current._element)
            current = current._next
        return '{}'.format(outcome)

    def _insert_between(self,e,predecessor,successor):
        node = super()._insert_between(e,predecessor,successor)
        return self._make_position(node)

    def add_first(self,e):
        return self._insert_between(e,self._header,self._header._next)

    def add_last(self,e):
        return self._insert_between(e,self._trailer._previous,self._trailer)

    def add_before(self,p,e):
        original = self._validate(p)
        return self._insert_between(e, original._previous, original)

    def add_after(self,p,e):
        original = self._validate(p)
        return self._insert_between(e,original, original._next)

    def delete(self,p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self,p,e):
        original - self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

# C37
def summing(self,value):
    a = self.first()
    b = self.after(a)
    while b:
        if a.element() + b.element() == value:
            return a,b
        else:
            a = b
            b = self.after(b)
    return

# C38


# C39


# C40
Non-Coding

# C41
Non-Coding

# C42


# C43


# P44


# P45


# P46


# P47

