#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/valid-anagram/

# 一開始可以用集合概念去做，但是還是有些情況要去cover，像是s = "aacc", t =
# "ccac"這種，集合都長一樣，但是組成元素個素不同，所以就要下去算每一個的個數

# s = "anagram"
# t = "nagaram"
# s = "rat"
# t = "car"
s = "aacc"
t = "ccac"

# 先用集合概念去做，如果連集合都長不一樣直接打掉。
if set(s) & set(t) != set(s) or set(s) & set(t) != set(t):
    print "False"
    exit()

# 走到這裡代表集合長一樣，就必須要下去一個一個看，看每一個元素個數有無相同
for i in set(s):
    print i
    if s.count(i) != t.count(i):        # 遇到不同的就回傳錯誤
        print "False, {}, s = {}, t = {}".format(i, s.count(i), t.count(i))
        exit()
# 會走到這裡代表完全一樣，回傳正確
print "True"
