#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/find-the-duplicate-number/

# Joma class講解Floyd解法
# https://www.youtube.com/watch?v=9YTjXqqJEFE

# nums = [1, 3, 4, 2, 2]
nums = [3, 1, 3, 4, 2]

# Floyd解法
tortoise = hare = nums[0]
while 1:
    tortoise = nums[tortoise]
    hare = nums[nums[hare]]
    if tortoise == hare:
        break
tortoise = nums[0]
while tortoise != hare:
    tortoise = nums[tortoise]
    hare = nums[hare]
print hare

# Hash解法
# Seen = set()
# for i in nums:
#     if i not in Seen:
#         Seen.add(i)
#     else:
#         print i
