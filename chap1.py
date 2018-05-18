#P29
import copy

def recFind(inputL):
    possL = list()
    for i in range(len(inputL)):
        currentI = [inputL[i]]
        remainder = inputL[:i] + inputL[i+1:]

        if len(remainder) == 0:
            return currentI
        else:
            returnL = copy.deepcopy(recFind(remainder))

            for j in returnL:
                tempCurrentI = copy.deepcopy(currentI)

                if isinstance(j, list):
                    for k in j:
                        tempCurrentI.append(k)
                    possL.append(tempCurrentI)
                else:
                    tempCurrentI.append(j)
                    possL.append(tempCurrentI)
    return possL
