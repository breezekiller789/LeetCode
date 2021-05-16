#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/longest-valid-parentheses/

# 左到右掃一次，然後再從右掃到左。


s = "(()"
s = ")()())"
# s = "()()"

left = 0
right = 0
maxLength = 0
for char in s:
    if char == "(":
        left += 1
    else:
        right += 1
    # 左括號數等於右括號數，代表有一個合法的配對
    if left == right:
        maxLength = max(maxLength, left+right)
    # 這一行很關鍵，因為從左掃到右，如果右括號大於左括號，現在這樣不可能是合法的
    # 所以全部重置。
    elif right > left:
        right = 0
        left = 0
right = 0
left = 0
for char in s[::-1]:
    if char == ")":
        right += 1
    else:
        left += 1
    # 左括號數等於右括號數，代表有一個合法的配對
    if left == right:
        maxLength = max(maxLength, left+right)
    # 這一行很關鍵，因為從右掃到左，跟上面相反而已。
    elif left > right:
        right = 0
        left = 0
print maxLength
