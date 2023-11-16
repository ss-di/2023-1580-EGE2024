
s = open('24_10105.txt').readline()
print(s[:5], s[-5:], len(s))
s = s[:-1] # s = s.strip()
print(s[:5], s[-5:], len(s))

#s = 'TAsTasdTgsdgTTxcjhgjhghjghjgjhgjhgjhgjhgjhgjhgjhg'

v = s.split('T')
print(v)

#for i in range(len(v)):
#    v[i] = len(v[i])
#print(v)

v = list(map(len, v))
#print(v)

mx = 0
for i in range(len(v)-100):
    #print(i, i+3)
    mx = max(mx, sum(v[i:i+101]))

print(mx+100)