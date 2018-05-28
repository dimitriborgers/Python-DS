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
    if len(S) > 0:
        total += (1/counter)
        counter += 1
        temp = har(S[1:], total, counter)
        return temp
    return total

# R7
Non-coding

# R8
Non-coding

# C9
def find(Seq):
    first = Seq[0]
    rest = Seq[1:]
    max_ = first
    min_ = first

    if len(rest) == 0:
        return first, first
    else:
        temp1,temp2 = find(rest)
        if temp1 > max_:
            max_ = temp1
        if temp2 < min_:
            min_ = temp2
    return max_, min_

# C10
Non-coding

# C11
def duplicates(S):
    first = S[0]
    rest = S[1:]

    if len(rest) == 0:
        return False
    else:
        temp = duplicates(rest)
        if temp == True:
            return True
        for i in rest:
            if i == first:
                return True
    return temp

# C12
def product(m,n):
    if m == 1:
        return n
    else:
        return n + product(m-1,n)

# C13
Non-coding

# C14
def hanoi(n, source, helper, target):
    print(source, helper, target)
    if n > 0:
        hanoi(n - 1, source, target, helper)
        if source:
            target.append(source.pop())
        hanoi(n - 1, helper, source, target)

# C15
def subsets(input_):
    outcome = [set(input_), set()]
    def pSubs(input_, total=[]):
        for i in range(len(input_)):
            first = [input_[i]]
            remainder = input_[:i] + input_[i + 1:]

            if len(remainder) == 1:
                if set(remainder) not in total:
                    total.append(set(remainder))
            else:
                pSubs(remainder, total)
                if set(remainder) not in total:
                    total.append(set(remainder))
        return total
    propers = pSubs(input_)
    for i in propers:
        outcome.append(i)
    return outcome

# C16
def reversering(input_):
    input_ = list(input_)

    def do(input_, first, last):
        if first < last:
            input_[first], input_[last] = input_[last], input_[first]
            do(input_, first+1, last-1)
        return input_

    outcome = do(input_, 0, len(input_)-1)
    return outcome

# C17
def palindrome(input1):
    list_input = list(input1)

    def reverser(input2, first, last):
        if first < last:
            input2[first], input2[last] = input2[last], input2[first]
            reverser(input2, first + 1, last - 1)
        return input2

    outcome = reverser(list_input, 0, len(list_input) - 1)
    if input1 == ''.join(outcome):
        return True
    return False

# C18
def vowel(input1, current = 0, vowels = 0, consonants = 0):
    input1 = list(input1)

    if current < len(input1):
        if input1[current] in ['a','e','i','u','o']:
            vowels += 1
        else:
            consonants += 1
        vowels, consonants = vowel(''.join(input1), current+1, vowels, consonants)
    return vowels, consonants

# C19
def rearrange(input1, first, last):
    if first != last:
        if input1[first] % 2 == 0:
            rearrange(input1, first+1, last)
        elif input1[last] % 2 == 1:
            rearrange(input1, first, last - 1)
        else:
            input1[first], input1[last] = input1[last], input1[first]
            rearrange(input1, first+1, last)
    return input1

# C20
def rearrange(input1, start, last, k):
    if start != last:
        if input1[start] < k:
            rearrange(input1, start+1, last, k)
        elif input1[last] > k:
            rearrange(input1, start, last-1, k)
        else:
            input1[start], input1[last] = input1[last], input1[start]
            rearrange(input1, start+1, last, k)
    return input1
"""Running time: O(n)"""

# C21
def summing(input1, first, last, k,temp = (None,None)):
    if first < last:
        if input1[first]*input1[last] == k:
            temp = (input1[first],input1[last])
            return temp
        else:
            temp = summing(input1, first, last-1, k)
            return temp
    elif first > last:
        return temp
    else:
        temp = summing(input1, first+1, len(input1)-1, k)
        return temp

# C22
Non-Coding

# P23
import os

def find(path, filename, total = []):
    if os.path.isdir(path):
        for file in os.listdir(path):
            childpath = os.path.join(path, file)
            if file == filename:
                total.append(childpath)
            find(childpath, filename, total)
    else:
        return total
    return total

# P24
def summation(S, U, temp = None):
    for i in U:
        if temp != None:
            return temp
        if len(S) == 7:
            dic = dict(zip(list(set('potpanbib')),S))
            if ((dic['p'] + dic['p'])*100) + ((dic['o']+dic['a'])*10)+(dic['t']+ dic['n']) == (dic['b']*100) + (dic['i']*10) + dic['b']:
                return dic
            else:
               return None
        else:
            U.remove(i)
            S.append(i)
            temp = summation(S, U)
            U.append(S.pop())
            U.sort()
    return temp

# P25
def ruler(inches, tick_length):
    for i in range(inches):
        print('-'*tick_length, i)
        counter, total, left = 1,0, tick_length - 1

        while left != 0:
            total += counter
            left -= 1
            counter *= 2
        list1 = [None]*total
        left = tick_length - 1

        half = int((total+1)/2)
        targets = [half]
        outcome = []
        difference = 0
        for i in range(left):
            for j in targets:
                if j == targets[0]:
                    difference = int(j/2)
                temp = left-i
                list1[(j-1)] = ('-'*temp)
                a,b = j - difference, j+difference
                outcome.append(a)
                outcome.append(b)
            targets = outcome
            outcome = []
        for i in list1:
            print(i)
    print('-'*tick_length, inches)

# P26
def hanoi(n, source, helper, target):
    print(source, helper, target)
    if n > 0:
        hanoi(n - 1, source, target, helper)
        if source:
            target.append(source.pop())
        hanoi(n - 1, helper, source, target)

# P27
import os

def walk(path, directories=[], files=[], start='/Users/dimitriborgers/Documents/Additional Courses',correct=False):
    if os.path.isdir(start):
        for filename in os.listdir(start):
            childpath = os.path.join(start, filename)
            if correct == True:
                if os.path.isdir(childpath):
                    directories.append(filename)
                else:
                    files.append(filename)
            else:
                if path == filename:
                    walk(path, start=childpath, correct=True)
                else:
                    walk(path,start=childpath)
    return directories, files
