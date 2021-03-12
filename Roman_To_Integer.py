# https://leetcode.com/problems/roman-to-integer/
# !/usr/bin/env python3
# -*- coding: utf-8 -*-


Dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s = "MDCXCV"
# Comprehension
m = [Dict.get(x) for x in list(s)]
print m
Sum = 0
i = 0
# 當這些羅馬數字全部排再一起的時候，把每一個字母的value全部抓出來之後，會發現一
# 個規律就是，如果左邊value小於右邊的時候，這時候就是右邊減掉左邊，舉例："IV"，
# 他們個別value是1, 5，左小於右，所以就是5-1=4，而如果是左大於右，就直接加起來就
# 好，例如："VIII"，5+1+1+1=8，這個while loop就是在做這件事情，剩下的東西就是在
# 避免index out of bounds而已。
while i < len(m):
    if i == len(m)-1:
        break
    if m[i] < m[i+1]:
        Sum += m[i+1] - m[i]
        i += 2  # 這邊i要加2的原因是這個iteration做完之後，下一個iteration就不用做
    else:
        Sum += m[i]
        i += 1
print i
# 這邊的if-else作用是，要解決"III"這種連續的，因為我的while loop在最後一個位置就
# 停下來了，不然會index out of bounds，阿這樣就還要檢查最後面那一個到底要不要加上
# 去
if i > len(m)-1:
    pass
else:
    Sum += m[i]
print Sum
