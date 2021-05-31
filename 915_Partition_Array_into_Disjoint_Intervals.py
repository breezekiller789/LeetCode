#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/partition-array-into-disjoint-intervals/

# 方法就是，走兩次，一次從頭到尾，一次從尾到頭，第一次掃就是在蒐集最大值，看到每
# 個位置為止所看到的最大值是多少全部用一個陣列存起來，再來就換尾巴掃到頭，也是一樣
# ，也是紀錄到每個位置為止所見的最小值，只是現在是反過來的。
# 都完成之後，我們就可以從這兩個陣列來看，如果發現某一個位置，他的最大值比到下個
# 位置為止的最小值還要小，那我們就找到了，這有一點點繞沒錯，但是就是這樣，因為其實
# 這個問題他可以是很簡單的，我寫了一個超簡單的程式，基本上就是這個問題的解法，只是
# 測資非常大，我會TLE，我原先寫的如下。
# for i in range(len(nums)):
#   if min(nums[i:]) > max(nums[:i]):
#       return i
# 可以看到只有三行而已，只要右半邊的最小值比左半邊的最大值還要大，那就找到了，
# 只是說這樣就會變成n^2，會TLE，用這個想法去變形，就會變成下面那樣的線性解法。

# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
nums = [5, 0, 3, 8, 6]

# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]
# nums = [1, 1, 1, 0, 6, 12]

# Output: 9
# nums = [90, 47, 69, 10, 43, 92, 31, 73, 61, 97]

# Output: 5
# nums = [1, 1, 1, 1, 0, 1]

# Output: 1
# nums = [1, 1]

length = len(nums)
Max = [0] * length
Min = [0] * length
currentMax = float("-inf")
currentMin = float("inf")

for i in range(length):
    currentMax = max(currentMax, nums[i])
    Max[i] = currentMax

for i in range(length-1, -1, -1):
    currentMin = min(currentMin, nums[i])
    Min[i] = currentMin
for i in range(length-1):
    if Max[i] <= Min[i+1]:
        print i+1
        exit()
print -1
