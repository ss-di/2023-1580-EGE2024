def hod(a, b, h, g):
    if a+b >= 77:
        if h % 2 == 1:
            return 1
        else:
            return 2
        
    h  = h + 1
    if h > g:
        return 3
    
    v = []
    v.append(hod(a+1, b, h, g))
    v.append(hod(a, b+1, h, g))
    v.append(hod(a*2, b, h, g))
    v.append(hod(a, b*2, h, g))
    
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
for b in range(1, 69+1):
    print(b, end="\t")
    for g in range(1, 5+1):
        print(hod(a, b, 0, g), end="\t")
    print()
