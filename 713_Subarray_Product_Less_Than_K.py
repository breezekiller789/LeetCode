#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/subarray-product-less-than-k/

# 這一題真不簡單，最關鍵就是 Count += right - left + 1這一行，很難想出來。


nums = [10, 5, 2, 6]
k = 100
product = 1
Count = 0
left = 0
right = 0
for idx, num in enumerate(nums):
    product *= num
    while product >= k:
        product /= nums[left]
        left += 1
    Count += right - left + 1       # 關鍵是這一句
    right += 1
print Count
