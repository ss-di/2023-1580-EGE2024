
s = open('24_10105.txt').readline()
print(s[:5], s[-5:], len(s))
s = s[:-1] # s = s.strip()
print(s[:5], s[-5:], len(s))

#s = 'TAsTasdTgsdgTTgjhg'

mx = 0
for i in range(len(s)):
    print(i/len(s)*100)
    input()
    for j in range(i, len(s)):
        ss = s[i:j+1]
        if ss.count('T') == 2:
            mx = max(mx, len(ss))

print(mx)