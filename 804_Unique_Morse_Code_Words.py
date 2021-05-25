#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/unique-morse-code-words/

# Hashing

# Output: 2
# Explanation:
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations, "--...-." and "--...--.".
words = ["gin", "zen", "gig", "msg"]

morseCode = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
    ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
    "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
]

hashMorseCode = {chr(ord('a')+value): morseCode[value] for value in range(26)}
hashResult = set()
for word in words:
    decodedString = ""
    for char in word:
        decodedString += hashMorseCode[char]
    hashResult.add(decodedString)
print len(hashResult)
