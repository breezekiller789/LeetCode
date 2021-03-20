#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/reverse-string/

# 練習過很多遍的反轉字串，有很多種方法，我就是用頭尾互換的方法，小心一下越界問題

# s = ["h", "e", "l", "l", "o"]
# s = ["c", "a", "b", "d"]
s = ["a"]
# =============Code Starts================= #
i = 0
length = len(s)-1
while i <= length/2:
    tmp = s[i]
    s[i] = s[length-i]
    s[length-i] = tmp
    i += 1
print s
