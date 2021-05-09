#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/reverse-words-in-a-string-iii/


s = "Let's take LeetCode contest"
strings = []
for string in s.split(" "):
    strings.append(string[::-1])
print " ".join(strings)
