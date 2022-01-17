"""
Note: This doesn't automatically parse the input file!
      You must parse it yourself.
      Watch this video for details: https://youtu.be/Eswmo7Y7C4U
"""

from itertools import product

with open("day24_1.in") as fin:
    raw_data = fin.read().strip().split("\n\n")[4:5]

steps = [6, 14, 13, None, 6, None, None, 3, None, 14, 4, None, None, None]
required = [None, None, None, 14, None, 0, 6, None, 3, None, None, 2, 9, 2]

# Part 1
# input_space = product(range(9, 0, -1), repeat=7)

# Part 2
input_space = product(range(1, 10), repeat=7)


def works(digits):
    z = 0
    res = [0] * 14

    digits_idx = 0

    for i in range(14):
        increment, mod_req = steps[i], required[i]

        if increment == None:
            assert mod_req != None
            res[i] = ((z % 26) - mod_req)
            z //= 26
            if not (1 <= res[i] <= 9):
                return False

        else:
            assert increment != None
            z = z * 26 + digits[digits_idx] + increment
            res[i] = digits[digits_idx]
            digits_idx += 1

    return res


for digits in input_space:
    res = works(digits)
    if res:
        print("".join([str(i) for i in res]))
        break