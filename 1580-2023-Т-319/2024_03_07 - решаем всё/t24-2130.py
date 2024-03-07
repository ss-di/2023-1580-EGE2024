def check(t):
    h = int(t[:2])
    m = int(t[2:])
    return h < 24 and m < 60

with open('24_2130.txt') as f:
    data = f.readline()
    
print(len(data), data[:10], data[-10:])

maxlen = 0
#0
curlen = 0
for i in range(len(data)-3, 4):
    if check(data[i:i+4]):
        curlen += 1
        maxlen = max(maxlen, curlen)
    else:
        curlen = 0
#1
curlen = 0
for i in range(1, len(data)-3, 4):
    if check(data[i:i+4]):
        curlen += 1
        maxlen = max(maxlen, curlen)
    else:
        curlen = 0
#2
curlen = 0
for i in range(2, len(data)-3, 4):
    if check(data[i:i+4]):
        curlen += 1
        maxlen = max(maxlen, curlen)
    else:
        curlen = 0
#3
curlen = 0
for i in range(3, len(data)-3, 4):
    if check(data[i:i+4]):
        curlen += 1
        maxlen = max(maxlen, curlen)
    else:
        curlen = 0
        
print(maxlen)        