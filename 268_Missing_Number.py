#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/missing-number/

# 知道list長度之後，就知道全部加起來應該是多少，我就代入下面的和公式，上底加下底
# 乘以高除以二，然後我再去扣掉input list加起來的和，這樣就知道少了誰。
# 0+1+2+3+...+n = (n+1)*n/2


def Sum_Equation(n):
    return (n+1)*n/2


nums = [0, 1, 4, 2]
n = len(nums)
Sum = 0
for i in nums:
    Sum += i
print Sum_Equation(n)-Sum
