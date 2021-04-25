n = 7
Count = 0
while n:
    n = n & (n-1)
    Count += 1
print Count
