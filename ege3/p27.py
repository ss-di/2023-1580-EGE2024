with open("27_A_14960.txt") as f:
    data = f.readlines()
print(len(data), data[:5], data[-5:])

data = list(map(int, data))
print(len(data), data[:5], data[-5:])

n = data[0]
del data[0]
print(len(data), n, data[:5], data[-5:])

mx_r = -20001
mn_len = n + 1
mx_e = -1
for s in range(n-1):
    for e in range(s+1, n):
        r = data[e] - data[s]
        le = e - s + 1
        if (r > mx_r) or \
           (r == mx_r and e > mx_e) or \
           (r == mx_r and e == mx_e and le < mn_len):
            mx_r = r
            mn_len = le
            mx_e = e

print(mn_len)
        