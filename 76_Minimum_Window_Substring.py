#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/minimum-window-substring/

# Solution: https://www.youtube.com/watch?v=eS6PZLjoaq8

# 用sliding window解加上hash table下去解，其實要用sliding window這個不會太難看出
# 來，但是難是難在說要怎麼去控制sliding window，什麼時候要擴增什麼時候要縮減。

# 實作方法就是一貫的sliding window作法，有一個left, right，指著左邊跟右邊，然後
# 我們遇到一個字元就把它加進我們的hash table裡面，加到我們目前為止已經符合目標
# 字串裡面所有的字串，這個判斷的行為我們寫成一個function叫做StillSatisfy，
# 這個就是回傳說我們現在的hash table是不是都含有目標字串的字元，有的話就回傳true
# ，否則false，一旦我們符合了，我們就開始縮減sliding window直到不符合為止，然後我
# 們繼續擴張sliding window，也就是讓right繼續往後走，為什麼我們一旦符合就要縮減
# sliding window，因為我們符合之後，如果right繼續走我們還是會一直符合，題目要的是
# 最短的，我們繼續擴張right只會變更常並不會變更短，所以我們就必須要縮減sliding
# window，這就是為什麼一符合就要移動left的原因。

# Output: "BANC"
s = "ADOBECODEBANC"
t = "ABC"

# Output: "a"
# s = "a"
# t = "a"

# Output: ""
s = "a"
t = "aa"


def StillSatisfy(s1, s2):
    for char in s2:
        if char not in s1 or s2[char] > s1[char]:
            return False
    return True


# 首先要hash 目標字串所有字元
charCountInT = dict()
for char in t:
    if char not in charCountInT:
        charCountInT[char] = 1
    else:
        charCountInT[char] += 1

left = 0
right = 0
sLength = len(s)
minLength = [float("inf"), (0, 0)]
charCountInS = dict()
for idx, char in enumerate(s):

    if char in charCountInS:
        charCountInS[char] += 1
    else:
        charCountInS[char] = 1

    # 一旦目前我們符合目標字串，我們就進去然後縮減sliding window
    while StillSatisfy(charCountInS, charCountInT) \
            and left < sLength and right < sLength:
        charCountInS[s[left]] -= 1  # 把sliding window的最左邊字元刪掉。

        if right-left < minLength[0]:   # 記錄最小值
            minLength = [right-left+1, (left, right)]

        left += 1   # 縮減sliding window

    right += 1
start, end = minLength[1]
print s[start:end+1] if minLength[0] != float("inf") else ""
