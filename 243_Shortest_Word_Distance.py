#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/shortest-word-distance/

# 1. loop through list once, if current word matches either word1 or word2,
# record the current position, and sub the word1' position and word2's position
# and remember to check those positions are not out of bounds

# ===========Code=============

# Test Cases

# wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
# word1 = "coding"
# word2 = "practice"

wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"

# wordsDict = ["a", "b", "c", "d", "d"]
# word1 = "a"
# word2 = "d"

Min = float("inf")
word1CurrentPosition = -1
word2CurrentPosition = -1
for idx, word in enumerate(wordsDict):
    if word == word1:
        word1CurrentPosition = idx
    elif word == word2:
        word2CurrentPosition = idx
    if word1CurrentPosition != -1 and word2CurrentPosition != -1:
        Min = min(Min, abs(word1CurrentPosition-word2CurrentPosition))

print Min


# My first thought, using recursion but TLE

# # 1. Use recursion to solve, each iteration just to check if distance is
# # smaller than Mininum, make Minimun global btw.
# # 2. If there is no word1 or word2 in the rest of list, return


# # ===========Code============

# # Test Cases

# # wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
# # word1 = "coding"
# # word2 = "practice"

# # wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
# # word1 = "makes"
# # word2 = "coding"

# wordsDict = ["a", "b", "c", "d", "d"]
# word1 = "a"
# word2 = "d"

# Min = float("inf")


# def SWD(List, w1, w2):
#     global Min
#     if w1 not in List or w2 not in List:
#         return
#     elif w1 in List and w2 in List:
#         SWD(List[1:], w1, w2)
#         currentDist = abs(List.index(w1)-List.index(w2))
#         if currentDist < Min:
#             Min = currentDist


# SWD(wordsDict, word1, word2)
# print Min
