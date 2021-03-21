#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/plus-one/

# array list先轉成整數，加一，再把整數轉成list回傳

digits = [1, 2, 3]
# digits = [9, 9]
# digits = [4, 3, 2, 1]

# ===========Code Starts=============

string_num = ""
for i in digits:
    string_num += str(i)
num = int(string_num)
num += 1
print [x for x in str(num)]
