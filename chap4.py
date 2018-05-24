# R1
Non-coding
"""implement maxAlg instead"""
def findMax(list1):
    first = list1[0]
    seq = list1[1:]
    max_ = first

    if len(seq) == 0:
        return first
    else:
        temp = findMax(seq)
        if temp > max_:
            max_ = temp
    return max_

# R2
Non-coding
"""implement power() instead"""
def power(x,n):
    if n == 1:
        return x
    else:
        return x*power(x,n-1)

# R3
Non-coding

# R4
Non-coding
"""implement reverse() instead"""
def reverseFunc(S, first, last):
    if first < last - 1:
        S[first], S[last-1] = S[last-1],S[first]
        reverseFunc(S, first + 1, last - 1)

# R5
Non-coding

# R6
Non-coding
"""implement Harmonic Number instead"""
def har(S, total=0, counter=1):
    print("This is the total, ", total)
    if len(S) > 0:
        total += (1/counter)
        counter += 1
        temp = har(S[1:], total, counter)
        print(temp)
        return temp
    return total

# R7
Non-coding
"""implement conversionALg instead"""


# R8
Non-coding

# C9


# C10


# C11


# C12


# C13


# C14


# C15


# C16


# C17


# C18


# C19


# C20


# C21


# C22


# P23


# P24


# P25


# P26


# P27

