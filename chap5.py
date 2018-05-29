# R1
import sys

data= []
for k in range(5):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in btyes: {1:4d}'.format(a,b))
    data.append(None)

# R2
import sys

data= []
current = 0
for k in range(20):
    a = len(data)
    b = sys.getsizeof(data)
    if b > current:
        current = b
        print('Length: {0:3d}; Size in btyes: {1:4d}'.format(a,b))
    data.append(None)

# R3
import sys

data= [i for i in range(20)]
for k in range(20):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in btyes: {1:4d}'.format(a,b))
    data.pop()

# R4
def __getitem__(self,k):
    if not -self.n <= k < self.n:
        raise IndexError('index error')
    elif -self.n<= k < 0:
        return self._A[k]
    else:
        return self._A[k]
# R5
Non-Coding

# R6
def insert(self, k, value):
    if self._n == self._capacity:
        B = self._make_array(2*self._capacity)
        for k in range(0,k):
            B[k] = self._A[k]
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A = B
        self._capacity = 2*self._capacity
    else:
        for h in range(self._n, k, -1):
            self._A[h] = self._A[h-1]
    self._A[k] = value
    self._n += 1

# R7
def printRepeating(arr, size):

    for i in range(size):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] *= -1
        else:
            print (abs(arr[i]), end = " ")

# R8
from time import time
def compute_average(n):
    data = [i for i in range(n)]
    start = time()
    data.pop(0)
    end = time()
    return (end-start)/n

# R9
Non-Coding

# R10
self._forward = ''.join([chr((k+shift)%26 + ord('A')) for k in range(26)])

# R11
def compute(n,total=0):
    try:
        for i in n:
            total += sum(i)
    except (IndexError, TypeError):
        print('something went wrong')
    return total

# R12
def compute(n,total=0):
    try:
        total = sum([sum(i) for i in n])
    except (IndexError, TypeError):
        print('something went wrong')
    return total

# C13
Non-Coding

# C14
import random

def ownS(list1, list2=[]):
    while len(list2) != len(list1):
        i = random.randrange(max(list1))
        if i not in list2:
            list2.append(i)
    return list2

# C15
Non-Coding

# C16
def __pop__(self):
    value = self._A[self._n-1]
    self._A[self._n-1] = None
    self._n -= 1
    if self._n < self._capacity/4:
        B = self._make_array(self._capacity/2)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity /= 2
    return value

# C17
Non-Coding

# C18
Non-Coding

# C19
Non-Coding

# C20
Non-Coding

# C21


# C22


# C23


# C24


# C25


# C26


# C27


# C28
Non-Coding

# C29


# C30


# C31


# P32


# P33


# P34


# P35


# P36


# P37



