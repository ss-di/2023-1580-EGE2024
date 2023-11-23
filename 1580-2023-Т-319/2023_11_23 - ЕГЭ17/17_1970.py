def is_simple(x):
    x = abs(x)
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1
    return cnt==2

def is_simple2(x):
    x = abs(x)
    if x == 1:
        return False
    cnt = 0
    for i in range(2, x//2+1):
        if x % i == 0:
            cnt += 1
    return cnt==0

def is_simple3(x):
    x = abs(x)
    if x == 1:
        return False
    cnt = 0
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            cnt += 1
    return cnt==0

for i in range(1, 100):
    if is_simple3(i):
        print(i)

# Прочитаем все строки из файла
data = open('17_1970.txt').readlines()
print(len(data), data[:3], data[-3:])

# Переведем каждую строку в число
data = list(map(int, data))
print(len(data), data[:3], data[-3:])

# Решим задачу

cnt = 0 # Количество пар
mx = -20001 # Максимальная сумма

for i in range(len(data)-1): # -1 для того, чтобы не выйти за границу массива
    if is_simple(data[i]) or is_simple(data[i+1]):
        cnt += 1
        mx = max(mx, data[i] +  data[i+1])
        
print(cnt, mx)
