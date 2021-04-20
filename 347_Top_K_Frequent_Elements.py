#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/top-k-frequent-elements/

nums = [1, 1, 1, 2, 2, 3]
k = 2
Sets = {}
for i in nums:
    if str(i) not in Sets:
        Sets[str(i)] = 1
    else:
        Sets[str(i)] += 1
print Sets
