#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# 用binary search，先把matrix每一個element取出來放在Array裡，然後Sort Array，
# 最後再用binary search就可以找到了。

matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 5

# ==============Code Starts===============

Array = []
for i in matrix:        # O(n^2)
    Array.extend(i)     # 先把matrix所有element都取出來

Array = sorted(Array)

low = 0
high = len(Array)-1
while low <= high:
    mid = (low+high)/2
    if mid+1 == k:
        print Array[mid]
        break
    elif mid+1 > k:
        high = mid - 1
    elif mid+1 < k:
        low = mid + 1
