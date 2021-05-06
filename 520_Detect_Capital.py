#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/detect-capital/


def isAllCapital(String):
    for char in String:
        if char.islower():
            return False
    return True


def isAllLowerCase(String):
    for char in String:
        if char.isupper():
            return False
    return True


word = "USA"
word = "FlaG"
word = "GoogLe"
if isAllCapital(word):
    print True
elif isAllLowerCase(word):
    print True
elif word[0].isupper() and isAllLowerCase(word[1:]):
    print True
else:
    print False
