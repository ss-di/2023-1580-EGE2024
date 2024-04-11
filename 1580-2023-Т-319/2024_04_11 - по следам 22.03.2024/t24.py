'''
№ 1761 Danov2102 (Уровень: Сложный)
(А. Богданов) Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите максимальную длину цепочки символов, являющуюся палиндромом. Например, в последовательности ZZZXYZYXXXZ длина цепочки будет 5: --Z+XYZYX+X--

Файлы к заданию:24.txtПоказать ответ
'''

with open('24_1761.txt') as f:
    s = f.readline();

mx = 0
for i in range(len(s)):
    if i % 1000 == 0:
        print (i/len(s)*100)
    cur = 1
    j = 1
    while i-j >=0 and i+j <len(s) and s[i-j] == s[i+j]:
        cur += 2
        j += 1
    mx = max(mx, cur)
    
    cur = 0
    j = 1
    while i-j+1 >=0 and i+j <len(s) and s[i-j+1] == s[i+j]:
        cur += 2
        j += 1
    mx = max(mx, cur)    
    
print(mx)