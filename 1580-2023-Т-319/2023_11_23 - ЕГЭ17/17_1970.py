
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
    if data[i] % 3 == 0 or data[i+1] % 3 == 0:
        cnt += 1
        mx = max(mx, data[i] +  data[i+1])
        
print(cnt, mx)
