def calc(f, t):
    if f == 11:
        return 0

    if f == t:
        return 1
    if f > t:
        return 0
    return calc(f+1, t) + calc(f*2, t) + calc(f**2, t)

print(calc(2, 20))