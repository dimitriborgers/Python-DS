# R1
# Non-coding

# R2
# Non-coding

# R3
# Non-coding

# R4
# class Flower:
#     def __init__(self, name, petals, price):
#         self.name = name
#         self.petals = petals
#         self.price = price

#     """return price of flower"""
#     def getPrice(self):
#         return self.price

#     """set price of flower"""
#     def setPrice(self, price):
#         self.price = price
#         return self.price

# if __name__ == '__main__':
#     flower1 = Flower("rose", 10, 3.99)

# R5
# def charge(self, price):
#     try:
#         if price + self._balance > self._limit:
#             return False
#         else:
#             self._balance += price
#             return True
#     except TypeError:
#         print('Must be a number')
#         raise

# def make_payment(self, amount):
#     try:
#         self._balance -= amount
#     except TypeError:
#         print('Must be number')

# R6
# def make_payment(self, amount):
#     try:
#         if amount < 0:
#             raise ValueError('Must be positive')
#         self._balance -= amount
#     except TypeError
#         print('Must be number')

# R7
# def __init__(self, customer, bank, acnt, limit, balance=0)

# R8
# Non-coding

# R9
# def __sub__(self, other):
#     if len(self) != len(other):
#         raise ValueError('Dimensions must agree')
#     result = Vector(len(self))
#     for j in range(len(self)):
#         resut[j] = self[j] - other[j]
#     return result

# R10
# def __neg__(self):
#     result = Vector(len(self))
#     for j in range(len(self)):
#         result[j] = -self[j]
#     return result

# R11
# Relies on __len__ member function, which only works with vectors.
# def __len__(self):
#     if isinstance(self, list):
#         return len(self)
#     else:
#         return len(self._coords)

# R12
# def __mul__(self, number):
#     if not isinstance(number, int):
#         raise TypeError("must be a number")
#     else:
#         result = Vector(len(self))
#         for j in range(len(self)):
#             result[j] = self[j] * number
#     return result

# R13

