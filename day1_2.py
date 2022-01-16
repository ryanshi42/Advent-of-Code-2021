import sys

with open('day1_1input.txt') as f:
    argList = f.readlines()
    prev0 = 9999
    prev1 = 9999
    prev2 = 9999
    count = 0
    counter = 0
    for arg in argList:
        if counter < 2:
            counter += 1
        elif prev0 + prev1 + prev2 < prev1 + prev2 + int(arg):
            count += 1
        prev0 = prev1
        prev1 = prev2
        prev2 = int(arg)
    print("count = " + str(count))