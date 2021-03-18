#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/number-of-1-bits/

# 分成正負數來做，正數最簡單，負數最複雜，正數直接做，負數的話我先把它用2's
# complement，我先把decimal轉成binary，然後invert所有bit，最後加一，最後再去算
# 1有幾個，就結束。

n = 12
if n > 0:
    bin_string = str(bin(n)[2:])
    print bin_string.count('1')
else:   # 負數的要用2's complement
    # 先做成binary，然後把零都補上去
    bin_string = str(bin(abs(n))[2:])   # 先轉正，在找binary
    full_string = ""                    # 這個待會要放32-bit字串
    for i in range(32-len(bin_string)):
        full_string += "0"              # 先補零
    full_string += bin_string           # 把剛剛的binary加上去

    Full_string_List = list(full_string)  # 因為python字串不能assign，所以轉list
    for i, char in enumerate(Full_string_List):
        if char == "0":
            Full_string_List[i] = "1"       # 0->1
        else:
            Full_string_List[i] = "0"       # 1->0

    # 最後加上一，這邊先加，因為待會要進去for loop iterate
    val = int(Full_string_List[-1]) + 1     # 加一
    carry = 0
    if val >= 2:        # 要進位
        carry = 1
        Full_string_List[-1] = "0"
    else:               # 不用進位直接算1就可以結束
        Full_string_List[-1] = "1"
        print Full_string_List.count("1")
        exit()

    # 從倒數第二個開始做，因為最後一個剛剛已經加了。
    for i in xrange(len(Full_string_List)-2, -1, -1):
        val = int(Full_string_List[i]) + carry
        if val >= 2:
            carry = 1
            Full_string_List[i] = "0"
        else:
            Full_string_List[i] = "1"
            break
    print Full_string_List.count("1")
