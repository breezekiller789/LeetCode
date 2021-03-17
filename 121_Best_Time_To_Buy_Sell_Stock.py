#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# 線性掃一次list，算出difference，接下來就做maximum subarray，ref 53題

# 測資
# prices = [7, 1, 5, 3, 6, 4]
# prices = []
# prices = [1]
prices = [2, 4, 1]


if not prices:          # 測資基本檢查
    print []
elif len(prices) == 1:  # 只有一筆資料不用做，直接回傳0
    print 0

array = []
# 先走一次list，算出difference
for i in range(len(prices)-1):
    array.append(prices[i+1] - prices[i])

# Maximum Subarray(Kadane's Algorithm)
max_Global = array[0]
max_Current = array[0]
for i in range(1, len(array)):
    max_Current = max(array[i], max_Current+array[i])
    if max_Current > max_Global:
        max_Global = max_Current
# 如果算出來虧錢，直接回傳零
if max_Global < 0:
    print 0
print max_Global
