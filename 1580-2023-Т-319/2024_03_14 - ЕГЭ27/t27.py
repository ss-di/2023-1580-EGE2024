#for i in range(len(data)-3):
#    for j in range(i+3, len(data)):
        
n = int(input())
data = [int(input()) for i in range(n)]

INF = 100000

buf = data[:3]
mins =  [INF] * 10
ans = INF
for x in data[3:]:
    mins[buf[0] % 10] = min(mins[buf[0] % 10], buf[0])
    del buf[0]
    buf.append(x)
    for d in range(10):
        if (x + d) % 10 == 4 and x + mins[d] < ans:
            ans = x + mins[d]
            
if ans == INF:
    ans = -1
print(ans)