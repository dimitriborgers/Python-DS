import copy

def recFind(inputL, level = 1, possL = list(), final = list()):
    for i in range(len(inputL)):
        currentI = [inputL[i]]
        remainder = inputL[:i] + inputL[i+1:]
        print("This is currenI, ", currentI)
        print("This is remainder, ", remainder)
        print("This is the level, ", level)

        if len(remainder) == 0:
            return currentI
        else:
            level += 1
            returnL = copy.deepcopy(recFind(remainder, level, possL, final))
            level -= 1
            print("This is the level2, ", level)
            print("This is returnL, ",returnL)
            for j in returnL:
                print("This is j, ", j)
                tempCurrentI = copy.deepcopy(currentI)
                print("This is tempCurrentBefore, ", tempCurrentI)
                if isinstance(j, list):
                    for k in j:
                        tempCurrentI.append(k)
                        print("This is tempCurrentAfter, ", tempCurrentI)
                    possL.append(tempCurrentI)
                else:
                    tempCurrentI.append(j)
                    print("This is tempCurrentAfter2, ", tempCurrentI)
                    possL.append(tempCurrentI)
                print("This is possL, ", possL)
            print("reaching this point?")
        print("reaching this point?2")
        if level == 1:
            for a in possL:
                if len(a) == len(inputL):
                    final.append(a)
            possL = list()
            print("this is final", final)
    print("reaching this point?3")
    level -= 1
    return possL

print("start")
print(recFind([1,2,3,4]))
