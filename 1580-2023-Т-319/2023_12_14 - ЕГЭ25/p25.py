import fnmatch
# 1?2157***4
# 10 000 000 000

mx = 10**10

ans = []

for v in range(10):
    num = int(f'1{v}21574')
    if num % 2024 == 0:
        ans.append(num)
    for d in range(1, 4):
        for z in range(0, 10**d):
            zs = str(z)
            z = '0' * (d - len(zs)) + zs
            num = int(f'1{v}2157{z}4')
            if num % 2024 == 0:
                ans.append(num)
        
ans.sort()
for x in ans:
    print(x, x // 2024)
   
   
ans2 = []
st = 1021574
while st % 2024: # != 0
    st += 1
# 012345
# 1?2157***4
for x in range(st, mx+1, 2024):
    sx = str(x)
    if sx[0] == '1' and sx[2:6] == '2157' and sx[-1] == '4':
        ans2.append(x)
        
print(ans == ans2)

ans3= []
st = 1021574
st += (2024 - st % 2024) % 2024
# 012345
# 1?2157***4
for x in range(st, mx+1, 2024):
    sx = str(x)
    if fnmatch.fnmatch(sx, '1?2157*4'):
        ans3.append(x)

print(ans == ans3)
