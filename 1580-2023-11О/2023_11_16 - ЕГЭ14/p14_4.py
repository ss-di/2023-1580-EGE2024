def to10(x, n, d):
    x = x[::-1]
    res = 0
    for i in range(len(x)):
        res += d.index(x[i])*n**i
    return res

# 76543210
# 12x643y7
#n = '12x643y7'

digs = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
digs = sorted(digs) + ['+']
# print(sorted(digs))

for x in digs:
    for y in digs:
        num = to10(f'12{x}643{y}7', 37, digs)
        if num % 36 == 0:
            print(num, x, y, digs.index(x), digs.index(y), digs.index(y)*37 + digs.index(x))