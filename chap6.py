# R1
3,8,2,1,6,7,4,9

# R2
18

# R3
def transfer(S,T):
    for i in range(len(S)):
        temp = S.pop()
        T.append(temp)
    return S,T

# R4
def rec(S):
    if len(S) == 1:
        S.pop()
    else:
        S.pop()
        rec(S)
    return S

# R5
def reverser(Seq, Sta = []):
    for i in range(len(Seq)):
        Sta.append(Seq.pop(0))
    for i in range(len(Sta)):
        Seq.append(Sta.pop())
    return Seq

# R6
"""implement code instead"""
def match(Seq, Stack=[]):
    left = "{[("
    right = "}])"
    for i in Seq:
        if i in left:
            Stack.append(i)
        elif i in right:
            temp = right.index(i)
            top = left.index(Stack.pop())
            if temp == top:
                continue
            else:
                print('error')
                break
        else:
            continue
    if Stack:
        print("error again")

# R7
5,3,2,8,9,1,7,6

# R8
22

# R9
Non-Coding

# R10
Non-Coding

# R11
from collections import deque
queue = deque([1,2,3])

# R12


# R13


# R14


# C15


# C16


# C17


# C18


# C19


# C20


# C21


# C22


# C23


# C24


# C25


# C26


# C27


# C28


# C29


# C30


# C31


# P32


# P33


# P34


# P35


# P36


# P37


