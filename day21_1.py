p1Start = 5
p2Start = 8
p1p = 0
p2p = 0

x = True
counter = 0

while p1p < 1000 and p2p < 1000:
    roll = (counter + 1) * 3 + 3
    if x:
        p1Start += roll
        while p1Start > 10:
            p1Start -= 10
        p1p += p1Start
        x = False
    else:
        p2Start += roll
        while p2Start > 10:
            p2Start -= 10
        p2p += p2Start
        x = True
    print(p1p, p2p)
    counter += 3

print(counter)
if p1p > p2p:
    print(p2p * counter)
else:
    print(p1p * counter)