#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

digits = "23"   # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# digits = ""     # []
# digits = "2"    # ["a","b","c"]


def RecursiveCombine(hashTable, digits):
    if len(digits) == 1:
        return hashTable[digits[0]]
    retString = RecursiveCombine(hashTable, digits[1:])
    newList = []
    for outsideChar in hashTable[digits[0]]:
        for char in retString:
            newList.append(outsideChar+char)
    return newList


hashTable = {
    "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs",
    "8": "tuv", "9": "wxyz"
}

if not digits:
    print []
    exit()
print RecursiveCombine(hashTable, digits)
