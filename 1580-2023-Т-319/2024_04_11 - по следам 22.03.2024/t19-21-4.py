wins = [[0]*400 for i in range(400)]

def hod (a, b, h, mh, k):
    global wins

    if h % 2 == 1 and wins[a][b] == 1:
        return 1
    if h % 2 == 1 and wins[a][b] == 2:
        return 2
    if h % 2 == 0 and wins[a][b] == 1:
        return 2
    if h % 2 == 0 and wins[a][b] == 2:
        return 1

    if a + b >= 192:
        if h % 2 == 1:
            return 1
        else:
            return 2
        
    h += 1
    if h > mh:
        return 3
    
    v = []
    if k >= 3: v.append(hod(a+3, b, h, mh, k-3))
    if k >= 3: v.append(hod(a, b+3, h, mh, k-3))
    if k >= 5: v.append(hod(a+5, b, h, mh, k-5))
    if k >= 5: v.append(hod(a, b+5, h, mh, k-5))
    if k >= 7: v.append(hod(a+7, b, h, mh, k-7))
    if k >= 7: v.append(hod(a, b+7, h, mh, k-7))
    if k >= a: v.append(hod(a*2, b, h, mh, k-a))
    if k >= b: v.append(hod(a, b*2, h, mh, k-b))
    
    if len(v) == 0:
        return 3
    
    if h % 2 == 1:
        if 1 in v:
            wins[a][b] = 1
            return 1
        elif 3 in v:
            return 3
        else:
            print('*')
            wins[a][b] = 2
            return 2
        
    else:
        if 2 in v:
            wins[a][b] = 1
            return 2
        elif 3 in v:
            return 3
        else:
            print('*')
            wins[a][b] = 2
            return 1
    
    
f = open('p19-21.txt', "w")

print(end='\t', file=f)
print(end='\t', file=f)
for mh in range(1, 7):
    print(mh, end='\t', file=f)
print(file=f)

for a in range(27, 28):
    for b in range(164, 0, -1):
        print(a, end='\t', file=f)
        print(b, end='\t', file=f)
        print(a, end='\t')
        print(b, end='\t')
        res = hod(a, b, 0, 256, 256)
        print(res, end='\t')
        print(res, end='\t', file=f)
        print(file=f)
        print()
f.close()

with open('p19-21-m.txt', "w") as f:
    for st in wins:
        for z in st:
            print(z, end=' ', file=f)
        print(file=f)
