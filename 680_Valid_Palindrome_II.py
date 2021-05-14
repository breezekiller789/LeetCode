#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/valid-palindrome-ii/


def isValid(s, low, high, alreadyDeleted):
    while low < high:
        if s[low] == s[high]:
            low += 1
            high -= 1
        else:
            if alreadyDeleted:
                return False

            # We delete one, either left or right
            return isValid(s, low+1, high, True) \
                or isValid(s, low, high-1, True)
    return True


s = "aba"
# s = "abca"
# s = "abc"
length = len(s)
print isValid(s, 0, length-1, False)
