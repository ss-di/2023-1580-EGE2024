
s = open('24_10724.txt').readline()
print(s[:5], s[-5:], len(s))
s = s[:-1] # s = s.strip()
print(s[:5], s[-5:], len(s))

#s = '0012300'

d = '0123456789ABCDEF'

l = 0
mx = 0

for i in range(len(s)):
    if s[i] in d:
        if not (l == 0 and s[i] == '0'):
            l += 1
        mx = max(mx, l)
    else:
        l = 0

print(mx)