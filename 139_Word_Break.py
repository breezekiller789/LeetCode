#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/word-break/

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


class TrieNode(object):
    def __init__(self):
        self.isWord = False
        self.children = dict()


root = TrieNode()
for word in wordDict:
    currentNode = root
    for char in word:
        if char not in currentNode.children:
            currentNode.children[char] = TrieNode()
        currentNode = currentNode.children[char]
    currentNode.isWord = True
print root.children
