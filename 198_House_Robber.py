#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/house-robber/

# Recursion + memoization

# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4
nums = [1, 2, 3, 1]

# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house
# 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12
nums = [2, 7, 9, 3, 1]


def RecursiveRobber(nums, start, alreadyChecked):
    if start >= len(nums):
        return 0
    elif alreadyChecked[start] is not None:
        return alreadyChecked[start]

    # 挑現在這個物品，然後去遞迴的偷下兩個，因為下一個不能偷了。
    pickedCurrent = RecursiveRobber(nums, start+2, alreadyChecked) + nums[start]
    # 現在這個不挑，去遞迴挑下一個。
    dontpickCurrent = RecursiveRobber(nums, start+1, alreadyChecked)

    # 看哪種結果比較好，放在陣列裡面，當作已經看過了，以後如果再看到就可以直接回
    # 傳，不用再繼續遞迴
    alreadyChecked[start] = max(pickedCurrent, dontpickCurrent)

    return alreadyChecked[start]


alreadyChecked = [None for _ in range(len(nums))]
print RecursiveRobber(nums, 0, alreadyChecked)
