def to10(x, n, d):
    x = x[::-1]
    res = 0
    for i in range(len(x)):
        res += d.index(x[i])*n**i
    return res

def from10(x, n, d):
    res = ''
    while x:
        res = d[x%n] + res
        x = x // n
    return res

digs = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
digs = sorted(digs) + ['+']
# print(sorted(digs))

print(to10(from10(11010101027377312, 37, digs), 37, digs))