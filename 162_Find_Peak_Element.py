#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/find-peak-element/

# 詳細註解都在程式碼當中，概念很簡單，其實就是邊界檢查比較困難，因為我們要在前後
# 新增一個無限小，所以整個index都要做shift

nums = [1, 2, 3, 1]
# nums = [1, 2, 1, 3, 5, 6, 4]
# nums = [2, 1]

# =============Code Starts============

# Base Case檢查。
if not nums or len(nums) == 1:
    print 0


nums.append(-float('inf'))          # 陣列前後都給他塞無限小。
nums.insert(0, -float('inf'))       # 陣列前後都給他塞無限小。
Peak_Candidate = []
for idx, num in enumerate(nums[1:-1], start=1):
    # 陣列先走一次，然後只要遇到peak就把他裝進Peak_Candidate陣列裡頭，記得裡面放
    # 的都是位置，不是放value，因為答案是要位置。
    if nums[idx] > nums[idx+1] and nums[idx] > nums[idx-1]:
        # 會要檢查這個idx有等於零的原因是因為，我們有在最前面多加一個元素，所以
        # 我們的整個index都要往前shift一個，阿這樣會導致如果peak落在陣列最前端，
        # 我存進去會變成-1，就是說它在加上無限小之前的位置是0，這樣我一存就變-1
        if idx <= 0:
            Peak_Candidate.append(0)
            continue
        Peak_Candidate.append(idx-1)    # 存的位置要減一，因為前面有多放無限小。

# 把所有peak候選人當中，挑一個value最大的，然後回傳他的位置。
Max = 0
for idx in Peak_Candidate:
    if nums[idx] > nums[Max]:
        Max = idx
print Max
