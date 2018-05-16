import copy

def recFind(inputL):
    for i in range(len(inputL)):
        currentI = [inputL[i]]
        remainder = inputL[:i] + inputL[i+1:]
        print("This is currenI, ", currentI)
        print("This is remainder, ", remainder)

        if len(remainder) == 0:
            return currentI
        else:
            returnL = copy.deepcopy(recFind(remainder))
            print("This is returnL, ",returnL)
            for j in returnL:
                print("This is returnL2, ", returnL)
                print("This is j, ", j)
                tempCurrentI = copy.deepcopy(currentI)
                print("This is tempCurrentBefore, ", tempCurrentI)
                if isinstance(j, list):
                    for k in j:
                        tempCurrentI.append(k)
                        print("This is tempCurrentAfter, ", tempCurrentI)
                    # tempCurrentI = copy.deepcopy(currentI)
                    possL.append(tempCurrentI)
                else:
                    tempCurrentI.append(j)
                    print("This is tempCurrentAfter2, ", tempCurrentI)
                    possL.append(tempCurrentI)
                print("This is possL, ", possL)
            print("reaching this point?")
    return possL

possL = list()
final = list()
print("start")
a = recFind([1,2,3,4])
for l in a:
    if len(l) == 3 and len(set(l)) == len(l):
        final.append(l)
print(len(final))

