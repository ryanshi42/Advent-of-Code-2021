import sys


with open('day1_1input.txt') as f:
    argList = f.readlines()
    prev = 9999
    count = 0
    for arg in argList:
        if int(arg) > int(prev):
            count += 1
        prev = arg
    print("count = " + str(count))