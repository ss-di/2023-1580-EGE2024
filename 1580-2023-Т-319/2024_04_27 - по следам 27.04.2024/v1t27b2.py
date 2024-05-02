with open('2_27_B.txt') as f:
    data = f.readlines()
    
print(len(data), data[:5], data[-5:])

data = list(map(int, data))
print(len(data), data[:5], data[-5:])

n = data[0]
del data[0]
print(n, len(data), data[:5], data[-5:])

k = 263

psum = [0]

mx_len = -1

for x in data:
    psum.append(psum[-1] + x)

for ost in range(k):
    #print(ost)
    mn_pos = -1
    for i in range(len(psum)):
        if psum[i] % k == ost:
            mn_pos = i
            break

    mx_pos = -1
    for i in range(len(psum)-1, -1, -1):
        if psum[i] % k == ost:
            mx_pos = i
            break
    
    mx_len = max(mx_len, mx_pos-mn_pos)
    print(ost, mx_len)

print(mx_len)