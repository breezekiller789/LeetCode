#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/3sum/

# 我是使用2SumII的方法下去做，也就是解答中Two Pointers的做法
# 按照上面的方法來做基本上就可以，但是還是有一些測資會有問題，例如一堆零的這種，
# 如果用解答做法會印出好幾個[0, 0, 0]，所以一開始我排序過後就直接把重複的0通通
# 都拿掉，因為多的零完全沒有用，但是其他的數有重複不可以亂拿。

nums = [0, 0, 0, 0]
# nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
# nums = [-1, 0, 1, 2, -1, -4]
# nums = [-1, 0, 1, 0]
nums = sorted(nums)     # 先排序
ans = []                # 放解答
if nums.count(0) >= 3:  # 有多個零
    ans.append([0, 0, 0])
for i in range(nums.count(0)-1):    # 把多的零拿掉，後面有-1是因為要留一個。
    nums.remove(0)
length = len(nums)
if length < 3:          # 長度小於三的話直接不要做
    print ans
    exit()
for i, pivot in enumerate(nums[:-2]):
    # 如果有重複的要跳過去
    if nums[i-1] == nums[i] and nums[i] != 0:
        continue
    low, high = i + 1, length - 1
    while low < high:
        Sum = nums[low] + pivot + nums[high]
        if Sum < 0:
            low += 1
        elif Sum > 0:
            high -= 1
        else:
            # 這段要多檢查如果ans裡面已經有該組合就不要再加進去。
            # 例如這個測資，[-1, -2, -2, -2, 3, 3, 3]
            # 這個如果沒有檢查，會出現多個[-1, -2, 3]
            tmp = [pivot, nums[low], nums[high]]
            if tmp in ans:
                low += 1
                high -= 1
                continue
            else:
                ans.append([pivot, nums[low], nums[high]])
                low += 1
                high -= 1
print ans
