# 76543210
# 12x643y7
#n = '12x643y7'

digs = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
digs = sorted(digs)
# print(sorted(digs))

for x in digs:
    for y in digs:
        num = int(f'12{x}643{y}7', 36)
        if num % 35 == 0:
            print(num, x, y, digs.index(x), digs.index(y), digs.index(y)*36 + digs.index(x))