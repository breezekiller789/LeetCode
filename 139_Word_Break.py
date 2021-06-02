#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/word-break/

# Recursion + Memoization

# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
s = "leetcode"
wordDict = ["leet", "code"]

# Output: true
# Explanation: Return true because "applepenapple" can be segmented as
# "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
s = "applepenapple"
wordDict = ["apple", "pen"]

# Output: false
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" + \
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" + \
    "aaaaaaaaaab"

wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa",
            "aaaaaaaaa", "aaaaaaaaaa"]

s = "catsandogcat"
wordDict = ["cats", "dog", "sand", "and", "cat", "an"]


def RecursiveBreak(s, hashTable, start, length, alreadyChecked):
    if length == start:
        return True
    # 從開頭慢慢往後擴展，如果有match字串的，就遞迴下去，看後面有沒有也是match
    for end in range(start, len(s)+1):
        if s[start:end+1] in hashTable and s[end+1:] not in alreadyChecked:
            ret = RecursiveBreak(s, hashTable, end+1, length, alreadyChecked)
            # 如果回傳true那就繼續往上回傳true就好
            if ret:
                return True
            # 這邊就是如果ret回傳False，代表回傳說我們現在end往後的字串就不可能
            # match，以後如果再遇到同樣的字串，不要再下去遞迴檢查。
            else:
                alreadyChecked.add(s[end+1:])
    return False


alreadyChecked = set()
hashTable = {word for word in wordDict}
length = len(s)
print RecursiveBreak(s, hashTable, 0, length, alreadyChecked)
