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
