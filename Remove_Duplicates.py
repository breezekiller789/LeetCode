#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# 這一題看起來很簡單，但是要注意，nums這個list他大小會隨著刪掉重複的元素進而
# 變小，所以上一個iteration的cur位置會是不一樣的，啊其實說穿了，根本不用去
# 動什麼東西，就只要把prev留著，cur往前一個就可以，啊如果要刪掉cur指到的元素，刪
# 之後cur不要去往前動，就讓它留著，不然cur往前一格之後指到的地方會是錯的

nums = [0,0,1,1,1,2,2,3,3,4]
#      [0,1,1,1,2,2,3,3,4]
#      [0,1,1,2,2,3,3,4]
#      [0,1,2,2,3,3,4]
#      [0,1,2,3,3,4]
#      [0,1,2,3,4]
prev = 0
cur = 1
length = len(nums)
while nums[cur] != None:
    # 兩個指標指著的東西不一樣，代表prev該往前了，prev往前之後cur也往前一格
    if nums[prev] != nums[cur]:
        prev = cur
        cur += 1
    # 這邊要小心，刪掉cur之後，cur不可以往前一格，因為刪掉一個元素，整個list會變
    else:
        del nums[cur]
    # 這個就是在做boundary check
    if cur == len(nums):
        break
print nums
