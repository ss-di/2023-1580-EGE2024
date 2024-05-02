with open('2_27_B.txt') as f:
    data = f.readlines()
    
print(len(data), data[:5], data[-5:])

data = list(map(int, data))
print(len(data), data[:5], data[-5:])

n = data[0]
del data[0]
print(n, len(data), data[:5], data[-5:])

k = 263

'''mx_sum = -1
mx_len = -1

for b in range(n):
    for e in range(b, n):
        cur_sum = sum(data[b : e+1])
        if cur_sum % k == 0 and e-b+1 > mx_len:
            mx_len = e-b+1
print(mx_len)'''

mx_lens = [-1] * k
mn_lens = [-1] * k

mn_lens[0] = 0

cur_sum = 0
for i in range(n):
    cur_sum += data[i]
    if mn_lens[cur_sum % k] == -1:
        mn_lens[cur_sum % k] = i+1
    mx_lens[cur_sum % k] = i+1

mx_len = -1
for i in range(k):
   if mn_lens[i] != -1 and mx_lens[i] != -1:
       if mx_lens[i] - mn_lens[i] > mx_len:
           mx_len = mx_lens[i] - mn_lens[i]
           
print(mx_len)