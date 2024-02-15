eng = "qwertyuiopasdfghjklzxcvbnm"
print(len(eng))
eng = list(eng)
print(eng)
eng.sort()
print(eng)
eng = ''.join(eng)
print(eng)

rus = "йцукенгшщзхъфывапролджэячсмитьбюё"
print(len(rus))
rus = list(rus)
print(rus)
rus.sort()
print(rus)
rus = ''.join(rus)
print(rus)

'''

_ _ _ _ _
8 8 8 8 8

'''

alf =  "ПРИВЫЧКА"
print(len(alf))
alf = list(alf)
print(alf)
alf.sort()
print(alf)
alf = ''.join(alf)
print(alf)

print(8**5)

words = []
for a1 in alf:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    words.append(a1+a2+a3+a4+a5)
                    
print(len(words), words[:10])


words2 = []
for i in range(len(words)):
    if (i+1) % 5 != 0:
        words2.append(words[i])

for i in range(len(words), -1, -1):
    if (i+1) % 5 == 0:
         del words[i]

print(len(words), words[:10])
print(len(words2), words2[:10])
print(words == words2)

def check(s):
    # "ПРИВЫЧКА"
    if "И" in s or "Ы" in s or "А" in s:
        return False
    
    for i in range(len(s)):
        if s.count(s[i]) != 1:
            return False
    
    return True

for i in range(len(words)):
    if check(words[i]):
        print(i+1, words[i])
        break

import itertools

s = "abc"

res = list(itertools.product(s, repeat=4))

for i in range(len(res)):
    res[i] = ''.join(res[i])

print(res)

res = list(itertools.permutations(s))

for i in range(len(res)):
    res[i] = ''.join(res[i])

print(res)

s = "aaa"
res = list(itertools.permutations(s))

for i in range(len(res)):
    res[i] = ''.join(res[i])

print(res)
res = set(res)
print(res)

res = list(res)
print(res)

s = "ПРОСТО"
res = list(itertools.permutations(s))

for i in range(len(res)):
    res[i] = ''.join(res[i])

print(len(res), res)
res = set(res)
print(len(res), res)

res = list(res)
print(len(res), res)

cnt = 0
for w in res:
    if 'ОО' not in w:
        cnt += 1
        
print(cnt)