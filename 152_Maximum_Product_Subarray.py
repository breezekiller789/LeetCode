#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/maximum-product-subarray/

# 這一題看起來跟Maximum Subarray很像，但是做起來差很多，首先，這題難就是難在說，他
# 裡面可能會有負數或者零在裡面，而這會造成很大的麻煩，就像原本很大的一個數，遇到一
# 個-1，瞬間從王子變成青蛙，但是如果待會又遇到一個-1的話，他就又從青蛙變回王子，所
# 以，我們必須要同時追蹤最小值，不可以只追蹤最大值，核心概念大概是這樣。
# 還有一個概念，就是DP，從上面講解來講，我們要從頭追蹤到尾，subarray在長大的時候，
# 會使用到上一個subarray，也就是子問題中有overlapping，而DP最大的元素就是要有
# Optimal Substructure，子問題要有交集才可以用，所以這一題才會用到DP

# nums = [2, 3, -2, 4]
nums = [-2, 0, 2, -3, -1]
# nums = [-100, 1, 2, 3, -1]

# ==========Code Starts===============

Res = nums[0]
Cur_Max = 1
Cur_Min = 1
for num in nums:
    if num == 0:
        Cur_Min, Cur_Max = 1, 1
        if Res < num:
            Res = num
        continue
    tmp = Cur_Max
    Cur_Max = max(Cur_Max * num, Cur_Min * num, num)
    Cur_Min = min(tmp * num, Cur_Min * num, num)
    Res = max(Res, Cur_Max)
print Res
