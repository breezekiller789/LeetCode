#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/rotate-image/

# 想法很簡單，就是線性代數的方法，row/column互換，要注意的地方就是迴圈的index，
# 當row > col不用做，換句話說就是，只要做對角線以上就好，一開始有遇到一個問題就是
# 沒有注意到這個，最後印出來跟原本一樣，原因就是上三角交換一次，下三角又交換一次
# 倒頭來還是一樣，剩下的最後就是把column互換，最左跟最右column互換，一步一步往裡
# 面互換，這樣做起來的效果就和旋轉一樣。

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
length = len(matrix)

# 先做轉置矩陣
for row in range(length):
    for col in range(length):
        # 只需做對角線以上的就好，對角線以下不用做
        if row >= col:
            continue
        # Swap三步驟
        tmp = matrix[row][col]
        matrix[row][col] = matrix[col][row]
        matrix[col][row] = tmp

# 把column交換，low/high分別代表最左跟最右邊，交換之後就low+1,
# high-1，往裡面的意思。
for i in range(length):
    low, high = 0, length-1
    # low == high時，代表矩陣是奇數大小，low > high時代表是偶數，兩種條件都要顧
    while low != high and low < high:
        tmp = matrix[i][low]
        matrix[i][low] = matrix[i][high]
        matrix[i][high] = tmp
        low += 1
        high -= 1
