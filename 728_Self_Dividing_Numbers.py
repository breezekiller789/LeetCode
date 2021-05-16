#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/self-dividing-numbers/

left = 1
right = 22
nums = [i for i in range(left, right+1)]
Ans = []
for num in nums:
    for char in str(num):
        if char == "0":
            break
        if num % int(char) != 0:
            break
    else:
        Ans.append(num)
print Ans
