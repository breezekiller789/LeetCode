#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/


def Longest_Subsequence(s1, s2):
    i = 0
    for char in s1:
        if i < len(s2) and char == s2[i]:
            i += 1
    return i


s = "abpcplea"
dictionary = ["ale", "apple", "monkey", "plea"]
# s = "abpcplea"
# dictionary = ["a", "b", "c"]
# s = "abce"
# dictionary = ["abe", "abc"]
s = "abpcplea"
dictionary = [
    "ale",
    "apple",
    "monkey",
    "plea",
    "abpcplaaa",
    "abpcllllll",
    "abccclllpppeeaaaa"
]


Max = ["", 0]
for string in dictionary:
    length = Longest_Subsequence(s, string)
    if length != len(string):
        continue
    if length > Max[1]:
        Max = [string, length]
    elif length == Max[1] and cmp(string, Max[0]) < 0:
        Max = [string, length]
print Max[0]
