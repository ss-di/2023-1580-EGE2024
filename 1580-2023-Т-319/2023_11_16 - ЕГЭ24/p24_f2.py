
s = open('24_21.txt').readline()
print(s[:5], s[-5:], len(s))
s = s[:-1] # s = s.strip()
print(s[:5], s[-5:], len(s))

l = 1
mx = 1

for i in range(1, len(s)):
    if s[i-1] != s[i]:
        l += 1
        mx = max(mx, l)
    else:
        l = 1

print(mx)