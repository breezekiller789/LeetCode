#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/single-number/

# 這題看似簡單，但是如果要追求線性時間、in place的話就不簡單，我的方法就類似
# hashing，用python的Dictionary來做，如果有一樣的就+1，最後看有哪個出現個數是1
# 就印那個

# nums = [2, 2, 1, 2, 2]
Dict = dict()
nums = [4, 1, 2, 1, 2]
for num in nums:
    # 出現過，把count+1
    if str(num) in Dict:
        Dict[str(num)] += 1
    # 沒出現過，就加進去
    else:
        Dict[str(num)] = 1
# 找出count == 1的印出來
for key in Dict:
    if Dict[str(key)] == 1:
        print key
    # print Dict[str(key)]
