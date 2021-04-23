#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/maximum-product-of-word-lengths/

words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
words = ["eae", "ea", "aaf", "bda", "fcf", "dc", "ac", "ce", "cefde", "dabae"]
words = ["a", "aa", "aaa", "aaaa"]


# Use bit operation to check if two strings have common character
# def Has_No_Common_Char(word1, word2):
#     word1BitPattern = 0
#     word2BitPattern = 0
#     for char in word1:
#         offset = ord(char) - ord('a')
#         word1BitPattern |= 1 << offset
#     for char in word2:
#         offset = ord(char) - ord('a')
#         word2BitPattern |= 1 << offset
#     return word1BitPattern & word2BitPattern == 0


# length = len(words)
# Max = float("-inf")

# for idx, word in enumerate(words):
#     j = idx+1
#     while j < length:
#         if Has_No_Common_Char(word, words[j]):
#             Max = max(Max, len(word)*len(words[j]))
#         j += 1
# if Max == float("-inf"):
#     print 0
#     exit()
# print Max


# My first thoughts, it works, works fine
sets = []
length = len(words)

for word in words:
    sets.append(set(word))

Max = float("-inf")
for idx, first in enumerate(words[:-1]):
    j = idx+1
    while j < length:
        if not sets[idx] & sets[j]:
            Max = max(Max, len(words[idx])*len(words[j]))
            print sets[idx], sets[j]
        j += 1
if Max == float("-inf"):
    print 0
    exit()
print Max
