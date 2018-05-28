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


# R8


# R9


# R10


# R11


# R12


# C13


# C14


# C15


# C16


# C17


# C18


# C19


# C20

