#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/longest-palindromic-substring/
s = "babad"
# s = "cbbd"
# s = "a"
# s = "ac"
s = "abcba"
s = "bbbba"


# My solution, very slow
def Expands(s, start, end, Strings):
    while start >= 0 and end < len(s) and s[start] == s[end]:
        string = s[start:end+1]
        if string not in Strings:
            Strings.add(string)
        start -= 1
        end += 1


Strings = set()
for idx, char in enumerate(s):
    Expands(s, idx, idx, Strings)
    Expands(s, idx, idx+1, Strings)
Max = [0, ""]
for string in Strings:
    if len(string) > Max[0]:
        Max = len(string), string
print Max[1]
