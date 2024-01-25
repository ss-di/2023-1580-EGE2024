f = open('26_24.txt') 
data = f.readlines()
f.close()

with open('26_24.txt') as f:
    data = f.readlines()

print(len(data), data[:3], data[-3:])

s, n = map(int, data[0].split())
del data[0]

print(len(data), data[:3], data[-3:], s, n)

data = list(map(int, data))
print(len(data), data[:3], data[-3:], s, n)

data.sort()
print(len(data), data[:3], data[-3:], s, n)

v = 0
cnt = 0
for i in range(n):
    if data[i] <= s - v:
        v += data[i]
        cnt += 1
        
print(cnt, v)
v -= data[cnt-1]
print(s-v)

mx = 0
for i in range(n):
    if data[i] <= s-v and data[i] > mx:
        mx = data[i]
print(mx)