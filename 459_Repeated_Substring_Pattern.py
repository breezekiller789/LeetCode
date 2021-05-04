#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/repeated-substring-pattern/

s = "ababc"
# s = "aba"
# s = "abcabcabcabc"
# s = "abcabcabc"

s_Length = len(s)
substringLength = 1
while substringLength < s_Length/2+1:
    subString = s[:substringLength]     # Get the current sub string

    # Because we want to multiply sub string, if s_Length is not multiple of
    # substringLength, then we don't have to do this round, go next directly
    if s_Length % substringLength != 0:
        substringLength += 1
        continue
    repeatedTimes = s_Length/substringLength    # Get the repeated times
    String = ""
    String += subString*repeatedTimes   # Now we get the whole string
    if String == s:     # Enter this if we get a perfect match
        print True
        exit()
    substringLength += 1
print False

# My Initial thoughts, very slow
# substringLength = 1
# s_Length = len(s)
# while substringLength < s_Length:
#     subString = s[:substringLength]
#     tmp = s.split(subString)
#     flag = False
#     for element in tmp:
#         if element:
#             flag = True
#     if not flag:
#         print not flag
#         exit()
#     # print s.split(subString), subString
#     substringLength += 1
# print not flag
