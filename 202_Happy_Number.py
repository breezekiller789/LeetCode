#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/happy-number/

# 把整數拆成字串，用無窮迴圈下去做，字串再每個去算平方和，然後再放進Seen，如果
# 已經出現在Seen代表輪迴了，直接跳出來，啊如果遇到1就代表找到，也是跳出來。

n = 19
Seen = []       # 代表這個數已經看過。
while 1:
    string = str(n)
    Sum = 0
    for i in string:    # 下去算平方和
        Sum += pow(int(i), 2)
    n = Sum
    if n == 1:          # 進去代表找到happy number
        print True
        break
    if n not in Seen:   # 進去代表這個數沒有看過
        Seen.append(n)
    else:               # 進去這裡代表已經遇到重複的了
        print False
        break
