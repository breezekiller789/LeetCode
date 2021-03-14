#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/powx-n/

# 原本以為超簡單，結果很多測資超乎我想像，首先，要考慮到floating point overflow
# 的問題，例如這種：x = 0.000001, n = 2147483647，如果傻傻的下去算，會直接TLE，
# 所以就要檢查，迴圈做的同時就檢查有沒有underflow，之前修數值分析就有學過，面對
# 浮點數不可以用 x == 0，要用interval的，因為浮點數可能是0.0000000123這樣是不會
# 等於零的。

x = -2
n = 2
result = 1.00000
# 先檢查n是偶數還是奇數，是偶數的話，x就可以直接轉成正的
if int(str(n)[-1]) % 2 == 0:
    x = abs(x)

# 再來就是檢查x他是不是超級接近1, -1，因為像是1.000000001這種，幾次方之後就under
# flow了，所以要先檢查
if x >= 1 and x >= -1.0000001:
    print 1
elif x <= -1 and x >= -1.0000001:
    print -1

# 到這邊就真的要去算了，正的次方跟負的次方要分開處理，一個是乘，一個是除
if n > 0:
    while n > 0:
        # 檢查有無underflow
        if result <= 0.000001 and result >= 0:
            break
        result *= x
        n -= 1
elif n < 0:
    while n < 0:
        # 檢查有無underflow
        if result <= 0.000001 and result >= 0:
            break
        result /= x
        n += 1
print result
