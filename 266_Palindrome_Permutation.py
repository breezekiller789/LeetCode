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


# Method on the cracking the coding interview
# 方法就是，其實我們變成在檢查雙數單數而已，而檢查雙數單數就像是在開電燈開關一樣，
# 只有開跟關，然而，我們如果第一次遇到這個字元，我們就把它所在位置的位元打開變成1，
# 如果第二次遇到，就把他關起來，變成0，下次遇到就再次設成1，這樣依此類推，然而，如
# 果這個字串s是一個合法的palindrom字串的話，最後他應該只剩下一個開關還開著，也就是
# 一個bit為1，或者全部都零，然而，要檢查一個binary是否只有一個1，就只要把它減一之後
# 跟自己做and，如果是零就是只有一個1，如果看不懂可以ref備忘錄的“LeetCode筆記”
bitVector = 0
for char in s:
    value = ord(char) - ord('a')
    mask = 1 << value
    if mask & bitVector == 0:
        bitVector |= mask
    else:
        bitVector &= ~mask
print bitVector & (bitVector-1) == 0


# Original method, works fine
# length = len(s)
# characters = {chr(ord('a')+x): 0 for x in range(26)}
# for char in s:
#     characters[char] += 1

# if length % 2 == 0:
#     for item in characters:
#         if characters[item] % 2 == 1:
#             print False
#             exit()
# else:
#     oddCount = 0
#     for item in characters:
#         if characters[item] % 2 == 1:
#             oddCount += 1
#             if oddCount > 1:
#                 print False
#                 exit()
# print True
