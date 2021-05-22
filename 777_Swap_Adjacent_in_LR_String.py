#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/swap-adjacent-in-lr-string/

# 這一題還真不好想，因為很難去發現線索，這一題的線索就是，R跟L他們彼此再怎麼換
# 位置也不會跨過彼此，就是說原本是RL相對位置，不可能換一換變成LR，所以線索1就有了
# 就是說start, end他們如果要match，他們所有R跟L的相對位置是不可能改變的，再來就是
# ，題目是XL->LX, RX->XR的關係，所以start開始在交換位置的時候，會發現其實L是一直
# 再往左邊遷移，R是在往右遷移的感覺，因為Ｌ被換到左邊，Ｒ被換到右邊，所以又可以
# 得到兩個線索，就是說如果一開始start裡面L的位置早就已經在end中相對應L的左邊了，
# 那就不可能會match，因為Ｌ只會往左邊走，那如果我一開始就在答案左邊了，那我還玩啥
# 我越走只會離答案越遠，Ｒ也是一樣只是反過來，如果start中Ｒ的位置已經在end相對應
# 的R的右邊，那也不用比了，因為Ｒ只會往右走，如果一開始就已經在答案的右邊，那根本
# 不用玩了。

# Output: true
start = "RXXLRXRXL"
end = "XRLXXRRLX"

# Output: false
# start = "X"
# end = "L"

# Output: false
# start = "LLR"
# end = "RRL"

# Output: true
# start = "XL"
# end = "LX"

# Output: false
# start = "XLLR"
# end = "LXLX"


A = [(char, idx) for idx, char in enumerate(start) if char != "X"]
B = [(char, idx) for idx, char in enumerate(end) if char != "X"]

# A and B doesn't have same length, no need to do anything, return false
if len(A) != len(B):
    print False
    exit()

for a, b in zip(A, B):
    # Ａ，Ｂ的字元相對位置根本不一樣的話，直接回傳false
    if a[0] != b[0]:
        print False
        exit()
    # start的Ｌ位置在end的左邊，不用比了直接回傳false
    if a[0] == "L" and a[1] < b[1]:
        print False
        exit()
    # start的Ｒ位置在end右邊，不用比了直接回傳false
    else:
        if a[0] == "R" and a[1] > b[1]:
            print False
            exit()
print True
