for i in range(len(data)):
    s = 0
    for j in range(i, len(data)):
        s = sum(data[i:j+1])
        if s % 43 == 0:
            ans += 1
        

mx = 0
ans = 0
for i in range(len(data)):
    s = 0
    for j in range(i, len(data)):
        s = s + data[j]
        if s % 43 == 0:
            if s > mx:
                mx = s
                ans = j-i+1
            elif s == mx and ans > j-i+1:
                ans = j-i+1
                
            
psum = [0]            
for x in data:
    psum.append(psum[-1] + x)
        
for i in range(len(data)):
    if i % 1000 == 0:
        print(i / len(data) * 100)
        
    for j in range(len(data), i, -1): # [i, j)
        s = psum[j] - psum[i]
        if s % 43 == 0:
            if s > mx or (s == mx and ans > j-i):
                mx = s
                ans = j-i
            break

#############################################
        k = 43
        psum = [0]
        lmax = [-1] * k
        lmin = [n+1] * k
        lmin[0] = 0
        
        for x in data:
            psum.append(psum[-1] + x)
            lmax[psum[-1] % k] = max(lmax[psum[-1] % k], len(psum)-1)
            lmin[psum[-1] % k] = min(lmin[psum[-1] % k], len(psum)-1)
        
        print(lmin)
        print(lmax)
        
        mxsum = -1
        mnlen = n+1
        for i in range(k):
            if lmin[i] != n+1 and lmax[i] != -1:
                if psum[lmax[i]] - psum[lmin[i]] > mxsum or \
                   psum[lmax[i]] - psum[lmin[i]] == mxsum and lmax[i] - lmin[i] < mnlen:
                    mxsum = psum[lmax[i]] - psum[lmin[i]]
                    mnlen = lmax[i] - lmin[i]
                    
        print(mnlen, mxsum)