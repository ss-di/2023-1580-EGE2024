def calc(f, t, p):
    if f == t and len(p) > 0:
        return 1
    if f in p:
        return 0
    
    return calc((f+1)%10, t, p + [f]) + \
           calc((f+3)%10, t, p + [f]) + \
           calc((f+7)%10, t, p + [f])

print(calc(1, 1, []))

p = [1]
n = p + [2]
print(p is n)