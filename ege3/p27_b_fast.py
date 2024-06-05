with open("27_B_14960.txt") as f:
    data = f.readlines()
print(len(data), data[:5], data[-5:])

data = list(map(int, data))
print(len(data), data[:5], data[-5:])

n = data[0]
del data[0]
print(len(data), n, data[:5], data[-5:])

mx = -10001
mn = 10001
mn_cur = 10001
for i in range(n):
    if data[i] <= mn_cur:
        mn_cur = data[i]
        mn_cur_p = i

    if data[i] >= mx:
        mx = data[i]
        mx_p = i
        mn = mn_cur
        mn_p = mn_cur_p

# 4 6 8 2 4 9 3
        
print(mx_p - mn_p + 1)
        