#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/number-of-matching-subsequences/

# 用Hashing + Two pointers

# Output: 3
s = "abcde"
words = ["a", "bb", "acd", "ace"]

# Output: 2
s = "dsahjpjauf"
words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]

hashTable = {char for char in s}
sLength = len(s)
Count = 0
alreadySeen = set()     # 已經看過然後不是的，就放進這裡，待會就直接跳過
justAddIt = set()       # 已經看過然後是s的subsequence，直接加一就跳下一個
for word in words:
    # 先前已經看過且不是，直接跳下一個。
    if word in alreadySeen:
        continue
    # 先前已經看過而且是s的子序列，加一之後跳下一個
    elif word in justAddIt:
        Count += 1
        continue
    sIndex = 0
    wordIndex = 0
    wordLength = len(word)
    while sIndex < sLength and wordIndex < wordLength:
        # 用two pointer
        if word[wordIndex] != s[sIndex]:
            sIndex += 1
        else:
            sIndex += 1
            wordIndex += 1
    # 如果word index走到底，代表word是s的子序列。
    if wordIndex == wordLength:
        Count += 1
        justAddIt.add(word)
    else:
        alreadySeen.add(word)
print Count
