''' Задача про "решето" на Питоне решается 45 секунд
Протокол
43.5675904750824 5761456
(59987268833891, 45313699) 2736056
(59986181309061, 45313391) 2736032
(59983190659751, 45312307) 2735966
(59982193792831, 45311971) 2735944
(59981196932931, 45311603) 2735922
45.74362635612488
'''

# ТЧ - 112667 Решето Эратосфена
import time
def resheto(N):
    A=[False,False,True,True]+[False,True]*(N//2)
    p=3
    B=[(2,2)]
    while p<=N:
        while A[p]==False : p+=2
        i=p*p
        B.append((B[-1][0]+p,p))
        while i<=N :
            A[i]=False
            i+=p
        p+=2
    return B
def ff(p): # маска 
    s=str(p)
    if s[0] != '5' or s[-1] !='1' : return False
    for j in ['309','319','329','339','349','359','369','379','389','399'] :
        if j in s :return True
    return False
t=time.time()
n=100000000
B=resheto(n)
print(time.time()-t,len(B))
k=5
m=len(B)-1
for i in range(m):
    if ff(B[m-i][0]) :
        print(B[m-i],m-i+1)
        k-=1
        if k<1 : break
print(time.time()-t)
