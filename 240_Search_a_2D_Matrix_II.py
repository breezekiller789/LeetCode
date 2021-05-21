#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/search-a-2d-matrix-ii/

# 這一題就不能用binary search，因為他每一列之間並不是有連續排序關係，他只有每一
# 列自己是排序關係，必須要所有都是連續排序關係才可以用binary search，所以這個
# 我們不能用binary search，但是可以用binary search相關的原理，就是
# "Prune and search"，就是把不可能的選項都去掉，篩選以及捨去法。

# 實作方法就是，我們從左下角開始當作起始點，不能從(0, 0)或(m, n)開始，一定要從
# 左下或右上開始，原因是因為左下跟右上他們每一步在做選擇的時候一定有兩種選擇，往
# 比較大的地方走或者往比較小的地方走，如果從(0, 0)開始，這樣會導致我們最一開始就
# 不知道到底要往右走還是往下走，因為往這兩個方向走都是變大，但是從左下或右上開始
# 就不會有這個問題。然而，每一步我們就跟目標比較，看目標比我現在位置還要大還是小
# ，如果目標比較大，那我們就知道我們不可以往上走，因為往上走我們會變更小，狀況只
# 會更糟，所以我們就要往右走，讓我們變大，反之，如果目標比較小，我們也會知道不可
# 能往右走，因為往右走我們會變大，也是變更糟糕，所以就是一定要往上走，就這樣執行
# 直到我們準備要越界，如果是要越界了還找不到，代表根本沒有這個目標，就回傳False

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 5
target = 20

m = len(matrix)
n = len(matrix[0])

startNode = (m-1, 0)
x, y = startNode
while True:
    # 目標比較小，往上走
    if matrix[x][y] > target:
        # 如果已經準備要越界了還找不到，就回傳false因為根本沒有這個target
        if x == 0:
            print False
            exit()
        x -= 1
    # 目標比較大，往右走
    elif matrix[x][y] < target:
        # 如果已經準備要越界了還找不到，就回傳false因為根本沒有這個target
        if y == n-1:
            print False
            exit()
        y += 1
    # 找到了
    else:
        print True
        exit()
