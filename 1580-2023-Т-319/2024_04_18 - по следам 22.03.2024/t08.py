def count(ld, g):
    if g == 0:
        return 1
    cnt = 0
    for d in range(ld-1, -1, -2):
        cnt += count(d, g-1)
    return cnt

ans = 0
for d in range(1, 16):
    ans += count(d, 11)
print(ans)