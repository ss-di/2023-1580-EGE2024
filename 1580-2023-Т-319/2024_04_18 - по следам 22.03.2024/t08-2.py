cnt = 0
for d1 in range(15, 0, -1):
    for d2 in range(d1-1, -1, -2):
        for d3 in range(d2-1, -1, -2):
            for d4 in range(d3-1, -1, -2):
                for d5 in range(d4-1, -1, -2):
                    for d6 in range(d5-1, -1, -2):
                        for d7 in range(d6-1, -1, -2):
                            for d8 in range(d7-1, -1, -2):
                                for d9 in range(d8-1, -1, -2):
                                    for d10 in range(d9-1, -1, -2):
                                        for d11 in range(d10-1, -1, -2):
                                            for d12 in range(d11-1, -1, -2):
                                                print(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12)
                                                cnt += 1
print(cnt)