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


# R5


# R6


# R7


# R8


# R9


# R10


# R11


# R12


# R13


# R14


# R15


# R16


# R17


# R18


# R19


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

