#P29
# import copy

# def recFind(inputL):
#     def find(inputL):
#         possL = list()
#         for i in range(len(inputL)):
#             currentI = [inputL[i]]
#             remainder = inputL[:i] + inputL[i+1:]

#             if len(remainder) == 0:
#                 return currentI
#             else:
#                 returnL = copy.deepcopy(recFind(remainder))

#                 for j in returnL:
#                     tempCurrentI = copy.deepcopy(currentI)

#                     if isinstance(j, list):
#                         for k in j:
#                             tempCurrentI.append(k)
#                         possL.append(tempCurrentI)
#                     else:
#                         tempCurrentI.append(j)
#                         possL.append(tempCurrentI)
#         return possL
#     return [''.join(b) for b in find(inputL)]

#P30
# def counter(number, count=0):
#     if number < 2:
#         raise ValueError('too small')
#     else:
#         while number >= 2:
#             number /= 2
#             count += 1
#     return count

# P31
# def makechange(charge, given):
#     difference = given - charge
#     hund = difference // 100
#     difference -= hund * 100
#     twenties = difference // 20
#     difference -= twenties * 20
#     return ('hundred bills {0} twenty bills {1}'.format(hund, twenties))

# P35
# from random import *

# def birthparadox(list1):
#     list2 = []
#     list3 = []
#     for i in list1:
#         for j in range(i):
#             list2.append(randrange(365))
#         if len(set(list2)) != len(list2):
#             list3.append('paradox')
#     return len(list3)/len(list1)

# print(birthparadox([5,10,15,20,15,30, 35, 40]))

#P36
# def counter():
#     dic = {}
#     for i in range(10):
#         inputted = input('input word ')
#         if inputted not in dic:
#             dic[inputted] = 1
#         else:
#             dic[inputted] += 1
#     return dic
# print(counter())
