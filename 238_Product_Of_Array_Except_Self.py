#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/product-of-array-except-self/

# 一開始先看有幾個零，兩個零以上不用做，沒有零最簡單，全部乘起來之後，用除的就
# 可以得到其他人的product，如果有一個零沒關係，就一樣全部乘起來，只是遇到零要略過
# ，最後直接把乘起來的值放到零的位置就好。


# 測資
nums = [1, 2, 3, 4]
# nums = [-1, 1, 0, -3, 3]
# nums = [1, 1, 1, 1, 0, 3, 3, 0, 0]

# 如果有兩個以上(含)的零，整個算完都會是零，不用做了，全放零就好了。
if nums.count(0) > 1:
    print [0 for i in range(len(nums))]
    exit()

# 到這裡代表只有一個或兩個零，然後我就先把全部product算完，但是遇到零要跳過去
All_Product = 1
Ans = []
for i in nums:
    if i == 0:      # 遇到零要跳過去，因為待會要放在零的那個位置。
        continue
    All_Product *= i

# 沒有零比較單純，直接做。
if nums.count(0) == 0:
    # 全部product算完之後，除以該值就是不包含自己，其他的product
    for i in nums:
        Ans.append(All_Product/i)
# 只有一個零，就把剛剛算出來的All_Product放到零的那個位置就好
else:
    Ans = [0 for i in range(len(nums))]
    Ans[nums.index(0)] = All_Product

print Ans
