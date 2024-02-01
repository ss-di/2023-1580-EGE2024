def hod(a, h, g, t):
    if a > 40:
        if h % 2 == 1:
            return 1
        else:
            return 2
        
    h  = h + 1
    if h > g:
        return 3
    
    v = []
    if t != 1: v.append(hod(a+3, h, g, 1))
    if t != 2: v.append(hod(a+6, h, g, 2))
    if t != 3: v.append(hod(a*2, h, g, 3))
    
    if h % 2 == 1:
        if 1 in v:
            return 1
        elif 3 in v:
            return 3
        else:
            return 2
    else:
        if 2 in v:
            return 2
        elif 3 in v:
            return 3
        else:
            return 1


print(end="\t")
for g in range(1, 5+1):
    print("x"+str(g), end="\t")
print()
a = 7
for b in range(2, 36+1):
    print(b, end="\t")
    for g in range(1, 5+1):
        print(hod(b, 0, g, 0), end="\t")
    print()
