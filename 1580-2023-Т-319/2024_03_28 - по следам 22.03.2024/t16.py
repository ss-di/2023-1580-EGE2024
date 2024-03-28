F = [0] * 70

for n in range(1, 69+1):
    if n < 3:
        F[n] = n
    else:
        F[n] = (2*n-1)*(F[n-1]+F[n-2])
        
print(F[69] % (10**9+7))


F = [0] * 70

for n in range(1, 69+1):
    if n < 3:
        F[n] = n
    else:
        F[n] = ((2*n-1)*(F[n-1]+F[n-2])) % (10**9+7)
        
print(F[69])