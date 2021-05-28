#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

# Sliding window

# Output: 3
# Explanation: The substring is "ece" with length 3.
s = "eceba"
k = 2

# Output: 2
# Explanation: The substring is "aa" with length 2.
# s = "aa"
# k = 1

# s = "abaccc"
# k = 2

seen = dict()
Max = float("-inf")
left = 0
right = 0
for i, char in enumerate(s):
    if char not in seen:
        seen[char] = 1
    else:
        seen[char] += 1
    while len(seen) > k:
        seen[s[left]] -= 1
        if seen[s[left]] == 0:
            del seen[s[left]]
        left += 1
    Max = max(Max, right-left+1)
    right += 1
print Max
