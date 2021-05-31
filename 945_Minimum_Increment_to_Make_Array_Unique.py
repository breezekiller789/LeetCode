#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/minimum-increment-to-make-array-unique/

# 先排序nums，然後每一次的迭代，所需要的步數只會是0，或者是我現在的值跟我應該要
# 的值的距離，如果我現在的值比我應該的值還要小，那就帶我表現在必須要increment了，
# 如果我現在的值比較大，那就代表我不用increment，然後我每一次都要更新我下一次所
# 應該的值，就是看現在應該的值加一跟現在的值加一比看誰大。

# Output: 1
# Explanation:  After 1 move, the array could be [1, 2, 3].
nums = [1, 2, 2]

# Output: 6
# Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to
# have all unique values
# nums = [3, 2, 1, 2, 1, 7]
# [1, 1, 2, 2, 3, 7]

# nums = [1, 1, 1, 1]

# nums = [999, 10, 123, 10000, 12345]
# [10, 123, 999, 10000, 12345]

moves = 0
needsToBe = 0
for num in sorted(nums):
    moves += max(needsToBe-num, 0)
    needsToBe = max(needsToBe+1, num+1)
print moves


# My initial thoughts, got TLE, the while loop takes too much time
# Seen = set()
# length = len(nums)
# moves = 0
# for i in range(length):
#     if nums[i] not in Seen:
#         Seen.add(nums[i])
#         continue

#     # nums[i] is seen before, keep increment until it's not seen
#     num = nums[i]
#     while num in Seen:
#         num += 1
#         moves += 1
#     Seen.add(num)
# print moves
