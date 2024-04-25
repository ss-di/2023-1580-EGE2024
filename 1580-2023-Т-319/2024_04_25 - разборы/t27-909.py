with open('27-A_909.txt') as f:
    data = f.readlines()

n = int(data[0])
del data[0]
for i in range(n):
    data[i] = sorted(list(map(int, data[i].split())))

print(n, data)

ans = 0
mn = 10001
for i in range(n):
    ans += sum(data[i][1:])
    if (data[i][2] - data[i][0]) % 5 != 0:
        mn = min(mn, data[i][2] - data[i][0])
    if (data[i][1] - data[i][0]) % 5 != 0:
        mn = min(mn, data[i][1] - data[i][0])
   
if ans % 5 != 0:
    print(ans)
else:
    print(ans-mn)

#25034 76468978

print(3**20)