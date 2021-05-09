#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/permutation-in-string/

# Ref question 438, using array, sliding window

s1 = "ab"
s2 = "eidbaooo"
# s1 = "ab"
# s2 = "eidboaoo"
# s1 = "abc"
# s2 = "cccccbabbbaaaa"

s1Length = len(s1)
s2Length = len(s2)
s1Count = [0 for _ in range(26)]
s2Count = [0 for _ in range(26)]

for char in s1:
    s1Count[ord(char)-ord('a')] += 1

for idx, char in enumerate(s2):
    s2Count[ord(char)-ord('a')] += 1
    if idx >= s1Length:
        s2Count[ord(s2[idx-s1Length])-ord('a')] -= 1
    if s2Count == s1Count:
        print True
        exit()
print False
