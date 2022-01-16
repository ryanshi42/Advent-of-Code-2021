import math

def calcDistTo(pos, argList):
    count = 0
    for arg in argList:
        n = abs(arg - pos)
        count += (n * (n + 1)) / 2
    return count

if __name__ == '__main__':
    argList = []
    with open('day7_1input.txt') as f:
        argList = [int(number) for number in f.readline().split(',')]
    
    # argList = [16,1,2,0,4,2,7,1,2,14]

    print(argList)

    lo = min(argList)
    hi = max(argList)

    while lo != hi:
        if calcDistTo(lo, argList) > calcDistTo(hi, argList):
            lo = math.ceil((lo + hi) / 2)
        elif calcDistTo(lo, argList) < calcDistTo(hi, argList):
            hi = math.floor((lo + hi) / 2)
        else:
            lo = hi
    print(calcDistTo(lo, argList))

