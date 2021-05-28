#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

# 先把原先陣列排序，放在一個新的陣列，然後我們下去比較，一次從頭到尾，一次從尾巴
# 到頭，一開始只要發現有不一樣，代表就是這個位置就是要排序的起始點，然後再從尾巴
# 掃到頭一次，也是有發現不一樣就代表這個位置是排序的終點，最後就算這段距離就可以

# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make
# the whole array sorted in ascending order.
nums = [2, 6, 4, 8, 10, 9, 15]

# Output: 0
# nums = [1, 2, 3, 4]

# Output: 0
# nums = [1]

# Output: 2
# nums = [1, 3, 2, 3, 3]

# Output: 4
# nums = [1, 3, 2, 2, 2]
#      [1, 2, 2, 2, 3]

sortedNums = sorted(nums)
prev = nums[0]
start = None
end = None
length = len(nums)

# 從頭到尾走一次
for i in range(length):
    if nums[i] != sortedNums[i]:
        start = i
        break
# 如果起始點還是空，代表原先已經排序
if start is None:
    print 0
    exit()
# 從尾到頭掃一次
for i in range(length-1, -1, -1):
    if nums[i] != sortedNums[i]:
        end = i
        break
print end - start + 1
