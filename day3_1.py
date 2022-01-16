def mode(lst):
    d = {}
    for a in lst:
        if not a in d:
            d[a]=1
        else:
            d[a]+=1
    return [k for k,v in d.items() if v==max(d.values())]

with open('day3_1input.txt') as f:
    argList = f.readlines()
    gammaRate = []
    allbits = []
    start = True
    for arg in argList:
        if start is True:
            start = False
            for i in range(len(arg)):
                allbits.append([arg[i]])       
        else:
            for i in range(len(arg)):
                allbits[i].append(arg[i])            
    bitModeList = []
    for bitColumn in allbits:
        bitModeList.append(mode(bitColumn))
    print(allbits)
    print(bitModeList)
    