def calc(f, t):
    if f == t:
        return 1
    if f > t:
        return 0
    return calc(f+1, t) + calc(f*2, t)

print(calc(1, 10) * calc(10, 20))