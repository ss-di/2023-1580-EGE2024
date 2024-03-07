'''
(Q -> A) * (A -> P)
(!Q + A) * (!A + P)

!Q*!A + !Q*P + A*!A + A*P

!Q*!A + !Q*P + A*P

!Q*P x = 1, 3, 5, 6, 7, 9

A*P + !Q*!A : 
A = (2, 4, 8, 10) + [1, 3, 5, 6, 7, 9]
'''
AllA = list(range(1, 11))

def check(A):
    Q = [2, 4, 8, 10]
    P = list(range(1, 11))
    for x in range(-10, 20):
        # (!Q + A) * (!A + P)
        if not (((not (x in Q)) or (x in A)) and \
           ((not (x in A)) or (x in P))):
            return False
        
    return True

ans = 0
for mask in range(2**len(AllA)):
    A = []
    for i in range(len(AllA)):
        if mask % 2 == 1:
            A.append(AllA[i])
        mask = mask // 2
    if check(A):
        ans += 1
print(ans)