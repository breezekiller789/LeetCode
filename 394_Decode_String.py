#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/decode-string/

# ===========Code===========

s = "3[a]2[bc]"
# s = "3[a2[c]]"
# s = "2[abc]3[cd]ef"
# s = "abc3[cd]xyz"
# s = "3[a2[b3[c4[d]]]]"

countStack = []
resultStack = []
resultString = ""
idx = 0
length = len(s)
while idx < length:
    # Parse the multiplier
    if s[idx].isdigit():
        multiplier = 0
        # Get the multiplier using top down approach
        while s[idx].isdigit():
            multiplier = 10 * multiplier + int(s[idx])
            idx += 1
        countStack.append(int(multiplier))
    # Push, keep the current string to the stack and reset resultString
    elif s[idx] == "[":
        resultStack.append(resultString)
        resultString = ""
        idx += 1
    # Pop
    elif s[idx] == "]":
        multiplicant = countStack.pop()
        string = resultStack.pop()
        for i in range(multiplicant):
            string += resultString
        resultString = string
        idx += 1
    # Enter this when this character is alphabet
    else:
        resultString += s[idx]
        idx += 1
print resultString
