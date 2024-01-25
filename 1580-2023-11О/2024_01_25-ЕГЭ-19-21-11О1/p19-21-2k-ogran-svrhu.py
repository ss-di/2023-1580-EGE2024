def hod(a, b, g, h):
    if a+b >= 77:
        if a+b < 90:
            if h % 2 == 1:
                return 1
            else:
                return 2
        else:
            if h % 2 == 1:
                return 2
            else:
                return 1

    h = h+1
    if h > g:
        return 3
    
    v = []
    v.append(hod(a, b+1, g, h))
    v.append(hod(a, b*2, g, h))
    v.append(hod(a+1, b, g, h))
    v.append(hod(a*2, b, g, h))
    
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

for s in range(1, 69+1):
    print(s, end='\t')
    for g in range(1, 5+1):
        print(hod(7, s, g, 0), end='\t')
    print()