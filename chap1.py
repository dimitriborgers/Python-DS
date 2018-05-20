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

# P32
# def calculator():
#     allL = list()
#     temL = list()
#     finished = False
#     while finished == False:
#         inputted = input('enter number, operator, or finish ')
#         if inputted == 'finish':
#             finished = True
#         else:
#             allL.append(inputted)
#             print(allL)
#     for i in range(len(allL)):
#         if allL[i] == '*':
#             times = int(allL[i-1])*int(allL[i+1])
#             temL.pop()
#             temL.append(times)
#         elif allL[i-1] == '*':
#             continue
#         elif allL[i] == '/':
#             divide = int(allL[i-1])/int(allL[i+1])
#             temL.pop()
#             temL.append(divide)
#         elif allL[i-1] == '/':
#             continue
#         else:
#             temL.append(allL[i])
#     allL = temL
#     temL = list()
#     for i in range(len(allL)):
#         if allL[i] == '+':
#             times = int(allL[i-1])+int(allL[i+1])
#             temL.pop()
#             temL.append(times)
#         elif allL[i-1] == '+':
#             continue
#         elif allL[i] == '-':
#             divide = int(allL[i-1]) - int(allL[i+1])
#             temL.pop()
#             temL.append(divide)
#         elif allL[i-1] == '-':
#             continue
#         else:
#             temL.append(allL[i])
#     return allL

# P33
# def calc(previous=None):
#     finished = False
#     list1 = []
#     if previous != None:
#         list1.append(previous)
#     while len(list1) < 3 and finished == False:
#         inputted = input('#, op, finish or clear ')
#         if inputted == 'clear':
#             calc()
#         elif inputted == 'finish':
#             finished = True
#         else:
#             list1.append(inputted)
#     if finished == False and isinstance(int(list1[0]), int) and isinstance(int(list1[2]), int) and list1[1] == '*':
#         temp = int(list1[0])*int(list1[2])
#         print(temp)
#         calc(temp)

# P34
# from random import *

# list2 = ['$','#','FLor','??']

# for i in range(100):
#     list1 = list('I will never spam my friends again')
#     randError = randrange(len(list1))
#     list1[randError] = choice(list2)
#     print(i+1,''.join(list1))

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
