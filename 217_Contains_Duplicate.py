#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/contains-duplicate/
# Joma class有講過這個，用一個演算法來做，線性時間，常數空間。
# https://www.youtube.com/watch?v=pKO9UjSeLew&ab_channel=JomaTech

# nums = [1, 2, 3, 1]
# nums = [1, 2, 3, 4]
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

# Hashing作法
# =================================
# hashmap = []
# for i in nums:
#     if i in hashmap:
#         return True
#     else:
#         hashmap.append(i)
# return False

# Sorting作法
# ============================
_sort = sorted(nums)
for i, num in enumerate(nums[:-1]):
    if _sort[i] == _sort[i+1]:
        print True
        exit()
print False
