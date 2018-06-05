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
9,5,9,4,7,4,8

# R13
def switch(D,Q):
    for i in range(len(D)):
        Q.append(D.popleft())

# R14
"""Same as R13"""

# C15
x = stack.pop()
x = max(x, stack.pop())

# C16
def __init__(self, maxlen=None):
    self._data = []
    self._maxlen = maxlen

def push(self, e):
    if self._maxlen <= len(self._data):
        raise Full('full')
    else:
        self._data.append(e)

# C17
def __init__(self, maxlen=None):
    self._data = [] if maxlen == None else [None]*maxlen
    self._maxlen = maxlen

# C18
def transfer(S,T,U):
    while S:
        T.append(S.pop())
    while T:
        U.append(T.pop())
    while U:
        S.append(U.pop())
    return S

# C19
tag = raw[j+1:k]
space = tag.find(' ')
if space:
    actual_tag = tag[:space]
else:
    actual_tag = tag

# C20
Johnson–Trotter algorithm

# C21
Non-Coding

# C22
Non-Coding
"""Implement function instead"""
def postfix(string, stack=[]):
    for i in string:
        if i is '*':
            stack.append(stack.pop()*stack.pop())
        elif i is '+':
            stack.append(stack.pop()+stack.pop())
        elif i is '-':
            temp = stack.pop()
            stack.append(stack.pop()-temp)
        elif i is '/':
            temp = stack.pop()
            stack.append(stack.pop()/temp)
        else:
            stack.append(int(i))
        print(stack)
    return stack

# C23
Non-Coding

# C24
Non-Coding
"""implement instead"""
from collections import deque

class Stack:
    def __init__(self):
        self._stack = deque([])
        self._storage = 0

    def push(self,e):
        self._stack.append(e)
        self._storage += 1

    def pop(self):
        temp = []
        while self._storage - 1 > 0:
            temp.append(self._stack.popleft())
            self._storage -= 1
        value = self._stack.popleft()
        self._stack.extend(temp)
        temp = []
        self._storage = len(self._stack)
        return value

    def top(self):
        return self._stack[-1]

# C25
Non-Coding


# C26
Non-Coding
"""implement instead"""
class Deque:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def add_first(self, e):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(e)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def add_last(self,e):
        self.stack1.append(e)

    def delete_first(self):
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        value = self.stack1.pop()
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return value

    def delete_last(self):
        return self.stack1.pop()

    def first(self):
        return self.stack1[0]

    def last(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0

    def __len__(self):
        return len(self.stack1)

# C27
Non-Coding
"""implement instead"""
from collections import deque

def check(S,X,found = False):
    Q = deque([])
    while S:
        temp = S.pop()
        if temp == X:
            found = True
        Q.append(temp)
    while Q:
        S.append(Q.popleft())
    while S:
        Q.append(S.pop())
    while Q:
        S.append(Q.popleft())
    return found, S

# C28
Same C16

# C29
def rotate(self):
    temp = self._data[self._front]
    self._data[self._front] = None
    self._front = (self._front + 1)%len(self._data)
    avail = (self._front + self.size-1)%len(self._data)
    self._data[avail] = temp

# C30
Non-Coding

# C31
Non-Coding

# P32


# P33


# P34
Same 22

# P35


# P36


# P37

