#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/find-all-anagrams-in-a-string/

"""
1. Use sliding window concept, and arrays. we prepare p_count at the first
place, which means occurence of each character of p, and we use this as a
reference. Then we scan through string s, add 1 to the position of that
character, and compare it to the reference array. But here comes a problem, we
have to move our sliding window, the way to do that, we just minus the start
of sliding window by 1, that performs the "moving sliding window" action.
"""

# ===========Code==========

s = "cbaebabacd"
p = "abc"
# s = "abab"
# p = "ab"

s_length = len(s)
p_length = len(p)
s_count = [0 for i in range(26)]
p_count = [0 for i in range(26)]
for idx in range(p_length):
    p_count[ord(p[idx])-ord('a')] += 1
Ans = []
for idx in range(s_length):
    s_count[ord(s[idx])-ord('a')] += 1
    if idx >= p_length:     # Move sliding window forward
        s_count[ord(s[idx-p_length])-ord('a')] -= 1
    if s_count == p_count:  # Enter this if the sliding window are matching
        Ans.append(idx-p_length+1)
print Ans

# My initial thoughts, got TLE:((
# p_hashTable = {}
# for char in p:
#     if char not in p_hashTable:
#         p_hashTable[char] = 1
#     else:
#         p_hashTable[char] += 1

# s_length = len(s)
# p_length = len(p)
# idx = 0
# Ans = []
# while idx < s_length-p_length+1:
#     shift = 0
#     s_hashTable = {}
#     while shift < p_length:
#         index = idx+shift
#         if s[index] not in s_hashTable:
#             s_hashTable[s[index]] = 1
#         else:
#             s_hashTable[s[index]] += 1
#         shift += 1
#     if s_hashTable == p_hashTable:
#         Ans.append(idx)
#     idx += 1
# print Ans
