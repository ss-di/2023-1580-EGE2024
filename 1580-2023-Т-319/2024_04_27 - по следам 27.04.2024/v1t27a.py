with open('1_27_A.txt') as f:
    data = f.readlines()
    
print(len(data), data[:5], data[-5:])

data = list(map(int, data))
print(len(data), data[:5], data[-5:])

n = data[0]
del data[0]
print(n, len(data), data[:5], data[-5:])

k = 137

mx_sum = -1
mx_len = -1

ans = []

for b in range(n):
    for e in range(b, n):
        cur_sum = sum(data[b : e+1])
        if cur_sum % k == 0 and \
           (cur_sum > mx_sum or \
            (cur_sum == mx_sum and e-b+1 > mx_len) ):
            mx_sum = cur_sum
            mx_len = e-b+1
            ans.append([mx_len, mx_sum])
print(mx_len, mx_sum)
print(ans)