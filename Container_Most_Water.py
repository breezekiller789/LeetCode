#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/container-with-most-water/

# 核心精髓就是，two pointers，一個指著最前面一個指著最後面，每一步都算出兩個指
# 標所圍出來的面積，算完之後比大小，如果發現是max就把max換成現在這個面積，重點
# 是，面積算完之後，就比較兩個指標的y座標高度，誰高度比較小誰就往前，比較小的人
# 往前的原因是，今天是算水的面積，一個容器裝滿水，如果有一邊比較短，水最滿就只會
# 是最短邊乘以底部長，最長那一邊是不會影響水面積，所以必須是短的那一邊移動而不是
# 長的那一邊，再來，萬一遇到兩邊都一樣長怎麼辦，只需要移動某一個指標就可以，左
# 右邊都可以，並不會影響答案。

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# height = [1, 1]
# height = [4, 3, 2, 1, 4]
# height = [1, 2, 1]
length = len(height)
low = 0
high = length - 1
Max = 0
while low < high:
    # max(目前最大面積, 現在兩個指標算出來的面積）
    Max = max(Max, min(height[low], height[high]) * (high - low))

    # 比較小的那邊往前移動
    if height[low] < height[high]:
        low += 1
    # 為了程式碼簡潔，如果後面較短或者一樣的話就統一移動high
    else:
        high -= 1
print Max
