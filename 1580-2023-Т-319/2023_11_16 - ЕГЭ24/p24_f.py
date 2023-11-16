
s = open('24_21.txt').readline()
print(s[:5], s[-5:], len(s))
s = s[:-1] # s = s.strip()
print(s[:5], s[-5:], len(s))

l = [s[0]]

mx = 1

for i in range(1, len(s)):
    if l[-1] !=s[i]:
        l.append(s[i])
        mx = max(mx, len(l))
    else:
        l = [s[i]]
        

print(mx)