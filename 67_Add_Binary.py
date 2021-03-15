#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/add-binary/

# 我是先把binary轉成十進位，兩數相加再換回去binary


# 把decimal轉成binary
def Bin_To_Dec(num):
    Sum = 0
    idx = 1
    num = list(num)
    while num:
        Sum += int(num.pop()) * idx
        idx *= 2
    return Sum


# binary -> decimal
def Dec_To_Bin(num):
    string = ""
    while num != 0:
        # print num, num % 2
        string += str(num % 2)
        num /= 2
    # 這個if是要解決萬一num = 0的時候，不可以回傳空字串，至少要回傳0
    if string:
        return string
    return "0"


a = "11"
b = "111"

num1 = Bin_To_Dec(a)
num2 = Bin_To_Dec(b)

print (Dec_To_Bin(num1+num2))[::-1]
