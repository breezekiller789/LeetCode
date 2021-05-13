#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/trapping-rain-water/

# Solution: https://www.youtube.com/watch?v=bu1quf2rOp8

# 想法就是，我們先找出最高牆壁，並找出他的位置，然後從左邊開始走，走到最高牆壁，
# 這途中我們要不停更新左半邊最高牆壁，因為我們要把雨水關起來，必須要左右兩邊都是
# 高的，這樣才能關住雨水。左邊算完了換右邊，右邊就是要從最尾巴往最高牆走，做法和
# 左邊一樣。

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]   # 6
height = [4, 2, 0, 3, 2, 5]                     # 9

Max = max(height)
maxIndex = height.index(Max)
leftHighestWall = 0
water = 0
for idx in range(maxIndex):
    if height[idx] > leftHighestWall:
        leftHighestWall = height[idx]
    else:
        water += leftHighestWall-height[idx]

rightHighestWall = 0
for idx in xrange(len(height)-1, maxIndex, -1):
    if height[idx] > rightHighestWall:
        rightHighestWall = height[idx]
    else:
        water += rightHighestWall-height[idx]
print water
