#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/accounts-merge/


nums = [1, 7, 3, 6, 5, 6]       # 3
nums = [1, 2, 3]                # -1
nums = [2, 1, -1]               # 0

Sum = sum(nums)     # Get the total sum
currentSum = 0
sumWithoutCurrent = 0   # 因為總和不包含pivot，所以要有這個變數紀錄這個以前的和
for idx, num in enumerate(nums):
    currentSum += num       # 記錄現在的總和
    if (Sum-num) % 2 == 1:  # 如果連偶數都不是，更新sumwithoutcurrent就好
        sumWithoutCurrent = currentSum
        continue
    else:
        # (Sum-num) is even number
        leftSupposedToBe = (Sum-num) / 2    # pivot以前應該要有的總值
        if leftSupposedToBe == sumWithoutCurrent:   # 如果match代表找到pivot
            print idx
            exit()
        sumWithoutCurrent = currentSum
# 走到這裡代表沒有pivot，回傳-1
print -1
