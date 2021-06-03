#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/decode-ways/

# Still have some bugs, but i'm very close

# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12)
s = "12"

# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or
# "BBF" (2 2 6)
# s = "226"

# Output: 0
# Explanation: There is no character that is mapped to a number starting with 0.
# The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of
# which start with 0.
# Hence, there are no valid ways to decode this since all digits need to be
# mapped
# s = "0"

# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero
# ("6" is different from "06")
# s = "06"


def RecursiveDecode(s, start, alreadyChecked):

    # Base case
    if start >= len(s):
        return 1
    elif start == len(s)-1 and s[-1] != '0':
        return 1
    if s[start] == '0':
        return 0

    # If already checked, return it
    if alreadyChecked[start]:
        return alreadyChecked[start]

    # Get the number of pattern recursively from start + 1
    numberOfPattern = RecursiveDecode(s, start+1, alreadyChecked)

    # If current 2 digits are valid, then we Recursively get the number of
    # start+2
    if int(s[start:start+2]) >= 1 and int(s[start:start+2]) <= 26:
        numberOfPattern += RecursiveDecode(s, start+2, alreadyChecked)

    # Memoization
    alreadyChecked[start] = numberOfPattern
    return numberOfPattern


alreadyChecked = [None for _ in range(len(s))]
print RecursiveDecode(s, 0, alreadyChecked)
