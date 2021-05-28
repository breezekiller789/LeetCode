#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/increasing-triplet-subsequence/

# 我完全參考Question 300 Longest increasing subsequence，但是TLE

# 另外一種解法比較不容易想出來，沒有用額外空間，線性時間。


# Output: true
nums = [1, 2, 3, 4, 5]

# Output: false
# nums = [5, 4, 3, 2, 1]

# Output: true
nums = [2, 1, 5, 0, 4, 6]


first = float("inf")
second = float("inf")
for num in nums:
    # first都會是維持在最小值。
    if num <= first:
        first = num
    # 會來這裡就是目前num比first還要大了，就把它當作我們的second
    elif num <= second:
        second = num
    # 會走到這裡代表num比first大，也比second要大，這就代表我們找到一個合法的了
    else:
        print True
        exit()
print False


# 我用DP解，結果TLE，我感覺是會對的，只是測資太大，裡面都是一堆[1, 2, 1, 2, 1,
# 2....]，導致我DP會一直算，算不完。
# length = len(nums)
# dp = [1 for _ in range(length)]

# for j in range(1, length):
#     for i in range(j):
#         if nums[j] > nums[i]:
#             dp[j] = max(dp[j], dp[i]+1)
#             if dp[j] == 3:
#                 print True
#                 exit()
# print False
