#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/search-a-2d-matrix/

# 這一題就是binary search，當初我會沒有做是因為我不知道怎麼套上binary
# search，因為他是二維陣列，但是其實就是只要看index就好，把陣列大小算出來，也
# 就是m*n，然後減一，這樣我們就可以算index，x = value/n, y = value%n，當初有想
# 到這樣但是還是不知道如何下手，沒想到我已經非常接近，算得到index，就可以放心
# 套上binary search了。

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3
# target = 13

m = len(matrix)
n = len(matrix[0])

low = 0
high = m * n - 1
while low <= high:
    mid = (low+high)/2
    x, y = mid / n, mid % n     # Transform value to index
    if matrix[x][y] > target:
        high = mid-1
    elif matrix[x][y] < target:
        low = mid+1
    else:
        print True
        exit()
print False
