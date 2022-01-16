argList = []

def equalStr(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    return set1 == set2

def subsetStr(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    return set1.issubset(set2)

with open("day8_1input.txt") as f:
    argList = f.readlines()
count = 0
for arg in argList:
    inputList = arg.split(" | ")[0].split(" ")
    outputList = arg.split(" | ")[1].split(" ")
    currDict = {}
    for input in inputList: 
        if len(input.strip()) == 2:
            currDict[1] = input.strip()
        elif len(input.strip()) == 3:
            currDict[7] = input.strip()
        elif len(input.strip()) == 4:
            currDict[4] = input.strip()
        elif len(input.strip()) == 7:
            currDict[8] = input.strip()
    
    for input in inputList:
        if len(input.strip()) == 6 and subsetStr(currDict[4], input.strip()):
            currDict[9] = input.strip()
        elif len(input.strip()) == 6 and subsetStr(currDict[1], input.strip()):
            currDict[0] = input.strip()
        elif len(input.strip()) == 6:
            currDict[6] = input.strip()

    for input in inputList:
        if len(input.strip()) == 5 and subsetStr(input.strip(), currDict[6]):
            currDict[5] = input.strip()
        elif len(input.strip()) == 5 and subsetStr(input.strip(), currDict[9]):
            currDict[3] = input.strip()
        elif len(input.strip()) == 5:
            currDict[2] = input.strip()

    i = 3
    for output in outputList:
        item = [k for k, v in currDict.items() if equalStr(v, output.strip())]
        count += item[0] * (10 ** i)
        i -= 1


print(count)