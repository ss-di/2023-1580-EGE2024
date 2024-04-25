import itertools

data = list(itertools.product([False, True], repeat=4))

for x, y, z, w in data:
    f = ((not x) and (not z or y) and (not w)) or \
        ((z == w) and (not (x or y) or w))
    if f:
        print(int(x), int(y), int(z), int(w), f)