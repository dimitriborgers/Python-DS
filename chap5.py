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
from time import time

letters = ''
with open('test.txt','r') as f:
    document = f.read()
start = time()
for c in document:
    if c.isalpha():
        letters += c
end = time()
print(end-start)

temp = []
start = time()
for c in document:
    if c.isalpha():
        temp.append(c)
    letters = ''.join(temp)
end = time()
print(start - end)

# C22
from time import time

data = [i for i in range(10000000)]
target = ['a','b']
target2 = ['a','b']
start = time()
for i in data:
    target.append(i)
end = time()
print(start-end)

start = time()
target2.extend(data)
end = time()
print(start-end)

# C23
from time import time

start = time()
data = [i for i in range(10000000)]
end = time()
print(start-end)

start = time()
target=[]
for i in range(10000000):
    target.append(i)
end = time()
print(start-end)

# C24
from time import time

data = [i for i in range(10000)]

start = time()
for i in range(int(len(data)/2)):
    data.remove(i)
end = time()
print(start-end)

data = [i for i in range(10000)]

start = time()
for i in range(int(len(data)/2)):
    data.remove(data[len(data)//2])
end = time()
print(start-end)

data = [i for i in range(10000)]

start = time()
for i in range(int(len(data)/2)):
    data.remove(data[len(data)-1])
end = time()
print(start-end)

# C25
def remove_all(data, value):
    original_length = len(data)
    for i in range(len(data)):
        if i > original_length-1:
            break
        while data[i] == value:
            data.remove(data[i])
            original_length -= 1
        print(data[i])

# C26
def find(seq):
    seq.sort()
    for i in range(len(seq)):
        if seq[i] == seq[i+1] == seq[i+2] == seq[i+3] == seq[i+4]:
            print(seq[i])
            break

# C27
Non-Coding

# C28
Non-Coding

# C29
def find(A,B,outcome=[]):
    for x in A:
        for y in B:
            if x[1] == y[0]:
                outcome.append([x[0],x[1],y[1]])
    return outcome

# C30
"""Running time: O(nlogn)"""
def mergesort(S):
    half = len(S)//2
    left = S[:half]
    right = S[half:]

    if half == 0:
        return right
    else:
        tempL = mergesort(left)
        tempR = mergesort(right)
        outcome = []
        currentL = 0
        currentR = 0
        while len(outcome) != len(tempL) + len(tempR):
            if currentL == len(tempL):
                outcome.append(tempR[currentR])
                currentR += 1
            elif currentR == len(tempR):
                outcome.append(tempL[currentL])
                currentL += 1
            elif tempL[currentL] <= tempR[currentR]:
                outcome.append(tempL[currentL])
                currentL += 1
            else:
                outcome.append(tempR[currentR])
                currentR += 1
        return outcome

# C31
def sum2D(S, outcome = 0):
    for i in S:
        if isinstance(i, list):
            tempSum = sum2D(i)
            outcome += tempSum
        else:
            outcome+=i
    return outcome

# P32
def sum3D(S, outcome=0):
    for i in S:
        for j in i:
            outcome += sum(j)
    return outcome
"""OR"""
def sum3D(S, outcome=0):
    dic = dict(zip([i for i in range(len(S))],[0]*len(S)))
    for i in S:
        for j in i:
            temp = len(j)
            counter = 0
            while counter < temp:
                dic[counter] += j[counter]
                counter += 1
    return dic

# P33
def _add(selfie, other):
    if len(selfie) == len(other):
        for x,y in zip(selfie, other):
            if len(x) == len(y):
                for i in range(len(x)):
                    x[i] += y[i]
            else:
                raise IndexError('not same')
        return selfie
    else:
        raise IndexError('not same')

# P34


# P35


# P36


# P37



