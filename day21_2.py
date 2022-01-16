p1s = 5
p2s = 8

p1 = 0
p2 = 0

x = True

winDict = {}

def getWin(pl, pr, p1s, p2s):
    if pl >= 21:
        return (1, 0)
    if pr >= 21:
        return (0, 1)
    if (pl, pr, p1s, p2s) in winDict:
        return winDict[(pl, pr, p1s, p2s)]
    ans = (0, 0)
    for i in [1, 2, 3]:
        for j in [1, 2, 3]:
            for k in [1, 2, 3]:
                np1s = (p1s + i + j + k ) 
                while np1s > 10:
                    np1s -= 10
                npl = pl + np1s
                b, c = getWin(pr, npl, p2s, np1s)
                ans = (ans[0] + c, ans[1] + b)
    winDict[(pl, pr, p1s, p2s)] = ans
    return ans

print(getWin(0, 0, p1s, p2s))