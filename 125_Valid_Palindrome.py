#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/valid-palindrome/

# 這題難在要把所有token都考慮進去，原本想用C寫，但是一malloc就給我heap overflow
# 所以還是用python寫


def Is_Palindrome(s):
    length = len(s)
    if length % 2 == 0:
        if s[:len(s)/2] == (s[len(s)/2:])[::-1]:
            return True
        # print s[:len(s)/2]
        # print (s[len(s)/2:])[::-1]
    else:
        if s[:len(s)/2] == (s[len(s)/2+1:])[::-1]:
            return True
        # print s[:len(s)/2]
        # print (s[len(s)/2+1:])[::-1]
    return False


# 把所有不是字母的都列出來，窮舉法，因為我不知道python如何用pointer，但是好像可
# 以用isalpha()來做。
tokens = [' ', ',', '\\', '.', '\'', '~', '+', '-', '[', ']', '(', ')', '<',
          '>', '*', '&', '^', '%', '$', '#', '@', '!', ':', '_', '{', '}',
          '"', '?', '/', ';', '`']
# s = "A man, a plan, a canal: Panama"
# s = "applee,,,&*&lppa"
# s = "avva"
# s = "avvva"
s = ""
s = s.lower()       # 先轉小寫
for i in tokens:
    s = s.replace(i, '')    # 過濾字串，只留字母
print Is_Palindrome(s)
