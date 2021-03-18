#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/majority-element/

# 線性走一次list，每一次就檢查dictionary中有無存在，有的話count+1，沒有則新增。
# 最後檢查誰的count > n/2就好了。

# nums = [3, 2, 3]
nums = [2, 2, 1, 1, 1, 2, 2]
# nums = []
length = 0
Dictionary = {}
for i in nums:
    if str(i) not in Dictionary:
        Dictionary[str(i)] = 1
    else:
        Dictionary[str(i)] += 1
    length += 1
print Dictionary
for i in Dictionary:
    if Dictionary.get(i) > length/2:
        print i
        exit()
