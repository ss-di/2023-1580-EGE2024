def hod(s, g, h):
    if s >= 29:
        if h % 2 == 1:
            return 1
        else:
            return 2

    h = h+1
    if h > g:
        return 3
    
    v = []
    v.append(hod(s+1, g, h))
    v.append(hod(s*2, g, h))
    
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


print(end='\t')
for i in range(1, 5+1):
    print(i, end='\t')
print()    

for s in range(1, 28+1):
    print(s, end='\t')
    for g in range(1, 5+1):
        print(hod(s, g, 0), end='\t')
    print()