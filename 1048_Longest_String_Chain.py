#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/longest-string-chain/

# Output: 4
# Explanation: One of the longest word chain is "a","ba","bda","bdca"
words = ["a", "b", "ba", "bca", "bda", "bdca"]

# Output: 5
words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]

dp = {}
for w in sorted(words, key=len):
    dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in xrange(len(w)))
print max(dp.values())
