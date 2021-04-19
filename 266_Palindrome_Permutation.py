#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/palindrome-permutation/

# Palindrome, so every character will occur even times except 1 character, the
# middle, but keep in mind, if length of string is even, there will be no middle
# character

s = "code"
# s = "aab"
# s = "carerac"
s = "ababc"
length = len(s)
characters = {chr(ord('a')+x): 0 for x in range(26)}
for char in s:
    characters[char] += 1

if length % 2 == 0:
    for item in characters:
        if characters[item] % 2 == 1:
            print False
            exit()
else:
    oddCount = 0
    for item in characters:
        if characters[item] % 2 == 1:
            oddCount += 1
            if oddCount > 1:
                print False
                exit()
print True
