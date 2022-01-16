def OxygenMode(lst):
    d = {}
    for a in lst:
        if not a in d:
            d[a]=1
        else:
            d[a]+=1
    returnList = [k for k,v in d.items() if v==max(d.values())]
    if len(returnList) > 1:
        return 1
    else:
        return returnList[0]

def CO2Mode(lst):
    d = {}
    for a in lst:
        if not a in d:
            d[a]=1
        else:
            d[a]+=1
    returnList = [k for k,v in d.items() if v==min(d.values())]
    if len(returnList) > 1:
        return 0
    else:
        return returnList[0]

with open('day3_1input.txt') as f:
    argList = f.readlines()
    allbits = []
    possibleNums = argList
    initials = ""
    i = 0
    while True:
        newPossibleNums = []
        for arg in possibleNums:
            if arg.startswith(initials):
                newPossibleNums.append(arg)
                allbits.append(arg[i]) 
        
        if len(possibleNums) == 1:
            break
        possibleNums = newPossibleNums

        initials += str(OxygenMode(allbits))
        #initials += str(CO2Mode(allbits))
        print(initials)
        i += 1
        allbits = []
    
        print(possibleNums)
    