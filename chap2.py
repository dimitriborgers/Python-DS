# R1
Non-coding

# R2
Non-coding

# R3
Non-coding

# R4
class Flower:
    def __init__(self, name, petals, price):
        self.name = name
        self.petals = petals
        self.price = price

    """return price of flower"""
    def getPrice(self):
        return self.price

    """set price of flower"""
    def setPrice(self, price):
        self.price = price
        return self.price

if __name__ == '__main__':
    flower1 = Flower("rose", 10, 3.99)

# R5
def charge(self, price):
    try:
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    except TypeError:
        print('Must be a number')
        raise

def make_payment(self, amount):
    try:
        self._balance -= amount
    except TypeError:
        print('Must be number')

# R6
def make_payment(self, amount):
    try:
        if amount < 0:
            raise ValueError('Must be positive')
        self._balance -= amount
    except TypeError
        print('Must be number')

# R7
def __init__(self, customer, bank, acnt, limit, balance=0)

# R8
Non-coding

# R9
def __sub__(self, other):
    if len(self) != len(other):
        raise ValueError('Dimensions must agree')
    result = Vector(len(self))
    for j in range(len(self)):
        resut[j] = self[j] - other[j]
    return result

# R10
def __neg__(self):
    result = Vector(len(self))
    for j in range(len(self)):
        result[j] = -self[j]
    return result

# R11
def __radd__(self, other):
    if len(self) != len(other):
        raise ValueError('dimensions must agree')
    result = Vector(len(self))
    for j in range(len(self)):
        result[j] = self[j] + other[j]
    return result

# R12
def __mul__(self, number):
    if not isinstance(number, int):
        raise TypeError("must be a number")
    else:
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * number
    return result

# R13
def __rmul__(self, number):
    if not isinstance(number, int):
        raise TypeError("must be a number")
    else:
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * number
    return result

# R14
def __mul__(self, other):
    if len(self) != len(other):
        raise ValueError('This does not work')
    else:
        result = 0
        for i in range(len(self))
        result += self[i]*other[i]
    return result

# R15
def __init__(self, d):
    if isinstance(d, int):
        self._coords = [0]*d
    else:
        self._coords = [0]*len(d)
        for i in range(len(self._coords)):
            self._coords[i] = d[i]

# R16
Non-coding

# R17
Non-coding
"""create class for example1 instead"""
class Mammal():
    def __init__(self,gender,age):
        self.gender = gender
        self.age = age

    def growOlder(self, number):
        self.age += number

    def getGender(self):
        return self.gender

class Goat(Mammal):
    def __init__(self,gender,age,farm):
        super().__init__(gender, age)
        self.farm = farm

    def growOlder(self, number):
        super().growOlder(number)

    def getAge(self):
        return self.age

# R18
a = FibonacciProgression()
list1 = []
while len(list1) != 8:
    temp = a._advnace()
    temp1 = list(temp)
    if temp1[0]==2 and temp[1]==2:
        list1.append(temp1)

# R19
Non-coding

# R20
Non-coding

# R21
Non-coding

# R22
def __eq__(self, other):
    if len(self) != len(other):
        raise ValueError('not compatible')
    else:
        for x,y in zip(self, other):
            if x != y:
                return False

# R23
def __lt__(self, other):
    if len(self) < len(other):
        return True
    elif: len(self) > len(other):
        return False
    else:
        for x,y in zip(self, other):
            if x > y:
                return False

# C24
Non-coding
"""Write an example for e-book instead"""
class Reader():
    def __init__(self, page):
        self.page = page

    def increment(self):
        self.page += 1
    def decrement(self):
        self.page -= 1
    def getPage(self):
        return self.page

# C25
def __mul__(self, other):
    if isinstance(other, int):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i]*other
    else:
        result = 0
        for x,y in zip(self, other):
            result += x*y

# C26
class ReversedSequenceIterator:
    def __init__(self, sequence):
        self.seq = sequence
        self.k = 0

    def __next__():
        self.k -= 1
        if abs(self.k) < len(self.seq) + 1:
            return self.seq[self.k]
        else:
            raise StopIteration()

# C27
def __contains__(self, k):
    if k < self.start or self.stop > k:
        return False
    else:
        if k % self.step == 0:
            return True
        else:
            return False

# C28
def __init__(self, customer, bank, acct, limit, apr, sur):
    super().__init__(customer, bank, acct, limit)
    self.apr = apr
    self.sur = sur

def charge(self, price):
    self.sur += 1
    success = super().charge(price)
    if not success:
        self.balance += 5
    if self.sur > 10:
        self. balance += 1
    return success

def process_monthly(self):
    self.sur = 0

# C29
def PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acct, limit, apr):
        super()__init__(customer, bank, acct, limit)
        self.apr = apr
        self.min = min

    def charge(self, price):
        success = super().charge(price)
        return success
    def process_monthly(self):
        if self._balance > 0:
            self.min = balance * 0.05
            self.balance += self.min

# C30
"""in CreditCard"""
def _set_balance(self,b):
    self._balance = b

"""in PredatoryCreditCard"""
    #do nothing

# C31
class Absolute(Progression):
    def __init__(self, start1 = 2, start2 = 200):
        self.start1 = start1
        self.start2 = start2

    def advance(self):
        self.start1 = abs(self.start2 - self.start1)
        self.start1, self.start2 = self.start2, self.start1

# C32
class sqrtProgression(Progression):

    def __init__(self, prev, start = 65536):
        super().__init__(start)
        self._prev = prev

    def _advance(self):
        self._prev = sqrt(self._current)
        self._current, self._prev = self._prev, self._current

# P33
import re

def poly(input, param):
    try:
        order = [i for i in list(input) if i == '+' or i == '-']
        input = re.split('\-|\+', input)
        for h in range(len(input)):
            if param not in input[h]:
                order[h-1] = None
        order = [i for i in order if i != None]
        input = [i for i in input if param in i]
        result = list()
        counter = 0

        for i in input:
            temp = list(i)
            temp2 = list()
            if int(temp[0]) in [i for i in range(10)]:
                temp2.append(temp[0])
            else:
                temp2.append('0')
            for j in range(1,len(temp)):
                if temp[j] == '^':
                    if temp[j-1] == param:
                        temp2[0] = str(int(temp2[0]) * int(temp[j+1]))
                        temp[j+1] = str(int(temp[j+1]) - 1)
                        temp2.append(temp[j])
                    else:
                        temp2.append(temp[j])
                elif temp[j] == param:
                    if len(i) <= j + 1:
                        continue
                    elif temp[j+1] != '^':
                         continue
                    else:
                        temp2.append(temp[j])
                else:
                    temp2.append(temp[j])
            for k in range(len(temp2)):
                if temp2[k] == '1':
                    del(temp2[k])
                    del(temp2[k-1])
                    break
            result.append(''.join(temp2))
            if len(order) > counter:
                result.append(order[counter])
            counter += 1
        result = ''.join(result)
        return result
    except:
        print('something went wrong')

print(poly('4x^8-3x^4y+3x^2y^2+5','x'))

# P34
def readFile(fileInput):
    alphabet = {}

    with open(fileInput, 'r') as f:
        data = f.read()

        data = list(data)
        data = [i.lower() for i in data if ord(i) in range(ord('a'),ord('z')) or ord(i) in range(ord('A'), ord('Z'))]
        total = len(data)
        print(total)
        for i in data:
            if i not in alphabet:
                alphabet[i] = 1 / total
            else:
                alphabet[i] += 1 / total
    return alphabet

# P35
import threading

class Package:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class User:
    def __init__(self, created = {}, recieved = []):
        self.cr = created
        self.re = recieved
        self.c = 0

    def createPack(self, name, size = 0):
        self.cr[str(name)] = Package(name, size)
        self.c += 1

    def sendPackage(self, person, package):
        sending = self.cr[package]
        person.re.append(sending)
        del(self.cr[package])

    def seeCreated(self):
        counter = 0
        for key,value in self.cr.items():
            print(counter, key)
            counter += 1

    def readPack(self):
        for i in self.re:
            print(i.size)
        self.re = list()

def looping(time, Alice, Bob):
    threading.Timer(time,looping,[time, Alice, Bob]).start()
    Alice.createPack('pack1',10)
    Alice.createPack('pack2',15)
    Alice.seeCreated()
    Alice.sendPackage(Bob, 'pack1')
    Alice.sendPackage(Bob, 'pack2')
    Bob.readPack()

def main():
    Alice = User()
    Bob = User()
    looping(3.0, Alice, Bob)

main()

# P36
import random

def create_list(size = 5):
    ecosystem = [random.choice([Animal('Bear'), Animal('Fish')]) for i in range(size)]
    for i in ecosystem:
        if i == None:
            print(i)
        else:
            print(i.type)
    print('----------')
    play(ecosystem)

def play(eco, counter = 0):
    if counter < 20:
        for i in range(len(eco)):
            print(eco[i])
            print('--------')
            if eco[i] != None:
                choice = eco[i].choose()
                print(choice)
                print(eco[i].type)
                print('---------')
                if choice =='left' and i == 0:
                    continue
                elif choice =='right' and i == len(eco) - 1:
                    continue
                elif choice =='stay':
                    continue
                else:
                    if choice =='left':
                        if eco[i-1] == None:
                            eco[i-1] = Animal(eco[i].type)
                        elif eco[i-1].type == eco[i].type:
                            temp = list()
                            if None in eco:
                                print(eco.index(None))
                                for j in range(len(eco)):
                                    if eco[j] == None:
                                        temp.append(j)
                                choice = random.choice(temp)
                                eco[choice] = Animal(eco[i].type)
                            else:
                                continue
                        elif eco[i-1].type == 'Bear' and eco[i].type == 'Fish':
                            eco[i] = None
                        elif eco[i-1].type == 'Fish' and eco[i].type == 'Bear':
                            eco[i-1] = None
                        else:
                            continue
                    elif choice =='right':
                        if eco[i+1] == None:
                            eco[i+1] = Animal(eco[i].type)
                        elif eco[i+1].type == eco[i].type:
                            print("get here")
                            temp = list()
                            if None in eco:
                                for j in range(len(eco)):
                                    if eco[j] == None:
                                        temp.append(j)
                                print(temp)
                                choice = random.choice(temp)
                                print(choice)
                                print(eco[choice])
                                eco[choice] = Animal(eco[i].type)
                                print("get here three")
                            else:
                                continue
                        elif eco[i+1].type == 'Bear' and eco[i].type == 'Fish':
                            eco[i] = None
                        elif eco[i+1].type == 'Fish' and eco[i].type == 'Bear':
                            eco[i+1] = None
                        else:
                            continue
                    else:
                        continue
            else:
                continue
            for i in eco:
                if i == None:
                    print(i)
                else:
                    print(i.type)
    else:
        return eco

class Animal:
    def __init__(self, type):
        self.type = type

    def choose(self):
        return random.choice(['left','right','stay'])

create_list()

# P37


# P38


# P39

