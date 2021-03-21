#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/first-unique-character-in-a-string/

# 因為可以假設全部都是alphabet且都是小寫，那這樣我就可以先準備一個26個位置的陣列
# 然後我走一次字串，我算出該字元與'a'的距離，代表該字元的位置，例如'c'，跟'a'距離
# 2，所以'c'會去array[2]+1，有點像是hashing，但是比hashing更簡單好實作，最後我再
# 走一次string，回去查看看count是不是1，是1就直接印。

# s = "leetcode"
s = "loveleetcode"

# ===============Code Start=================

Ans = [0 for i in range(26)]
for idx, char in enumerate(s):
    Ans[ord(char)-ord('a')] += 1
for idx, char in enumerate(s):
    if Ans[ord(char)-ord('a')] == 1:
        print char
        break
