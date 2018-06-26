# R1
current = a._head
while current._next._next != None:
    current = current._next

# R2
Non-Coding
"""implement instead"""
def mergeLL(a,b,c = SinglyLinkedList()):
    curr = a.head
    while curr:
        c.append(curr.data)
        curr = curr.next
    curr = b.head
    while curr:
        c.append(curr.data)
        curr = curr.next
    return c

# R3
Non-Coding
"""implement instead"""
def countNodes(LLhead, total = 1):
    if LLhead.next == None:
        return total
    else:
        total += 1
        return countNodes(LLhead.next, total)

# R4
Non-Coding
"""implement instead"""


# R5
def countNodes(CircularLL):
    current, current2 = CircularLL.head,CircularLL.head
    total = 1
    while current2.next != current:
        total += 1
        current2 = current2.next
    return total

# R6
Non-Coding

# R7
def rotate(LinkedQ):
    LinkedQ._tail._next = LinkedQ._head
    LinkedQ._head = LinkedQ._head._next
    LinkedQ._tail = LinkedQ._tail._next
    LInkedQ._tail._next = None

# R8
def middle(DLL):
    begin = DLL.header
    end = DLL.trailer
    while begin != end:
        if begin.next == end:
            return begin
        begin = begin.next
        end = end.next
    return begin

# R9
def mergeDLL(L,M):
    SLL = SinglyLinkedList()
    current = L.header.next
    while current != L.trailer:
        SLL.append(current)
        current = current.next
    while current != M.trailer:
        SLL.append(current)
        current = current.next
    return SLL

# R10
Non-Coding

# R11


# R12


# R13


# R14


# R15


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


# C25


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

