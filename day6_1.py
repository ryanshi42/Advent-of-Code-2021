# def calculate(fish, daysToLive):
#     curFish = 1
#     fish = int(fish)
#     remainingTime = max(0, daysToLive - fish)
#     if preCalcDict.get(remainingTime, 0) != 0:
#         return preCalcDict.get(remainingTime, 0)
#     while daysToLive > 0:
#         if fish == 0:
#             fish = 6
#             daysToLive -= 1
#             curFish += calculate(8, daysToLive)
#         else:
#             daysToLive -= fish
#             fish = 0
#     preCalcDict[remainingTime] = curFish
#     return curFish

# argList = []

# for line in open("day6_1input.txt"):
#     line = line.strip()
#     argList = line.split(',')

# # argList = [3,4,3,1,2]
# preCalcDict = {}
# daysToLive = 256
# totalNum = 0

# for fish in argList:
#     remainingTime = daysToLive - int(fish)
#     if preCalcDict.get(remainingTime, 0) == 0:
#         preCalcDict[remainingTime] = calculate(fish, daysToLive)
#     totalNum += preCalcDict[remainingTime]

# # print(preCalcDict)
# print(totalNum)

from typing import Counter


DAYS = 256

if __name__ == '__main__':
    with open('day6_1input.txt') as f:
        counter = Counter([int(number) for number in f.readline().split(',')])
    for _ in range(DAYS):
        counter = {
            0: counter[1],
            1: counter[2],
            2: counter[3],
            3: counter[4],
            4: counter[5],
            5: counter[6],
            6: counter[7] + counter[0],
            7: counter[8],
            8: counter[0]
        }
    print(sum(counter.values()))