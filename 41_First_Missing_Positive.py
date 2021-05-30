#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/first-missing-positive/

# 這一題解法跟Q.448很像

# Output: 3
nums = [1, 2, 0]

# Output: 2
nums = [3, 4, -1, 1]

# Output: 1
nums = [7, 8, 9, 11, 12]

length = len(nums)
if 1 not in nums:
    print 1
    exit()
# 我多放一個零進去，避免裡面沒有零，像是[1, 2]這種，我會印2，而不是3，多放一個零
# 進去就可以了
nums.append(0)
length += 1

# 把全部小於零的都改成1，可以這樣是因為我前面已經有檢查過了，現在nums裡面一定會
# 有1在裡面
for i in range(length):
    # 如果是零或者小於零，就給他1，不用怕1原本就不在，因為前面檢查過了，現在1一定
    # 在裡面
    if nums[i] < 0 or nums[i] == 0:
        nums[i] = 1

# 用index當作hash value，如果這個value在範圍裡面，就把這個value對應到的index的值
# 改成負的
for i in range(length):
    index = abs(nums[i])
    if index >= length:
        continue
    nums[index] = - abs(nums[index])

# 現在，從index 1開始，遇到正的值的話，代表那個index就是missing positive
for i in range(1, length):
    if nums[i] > 0:
        print i
        exit()

# 如果都有出現，那就是missing陣列大小。
print length

# 我這個方法可以AC但是我有用額外空間。
# Seen = [False] * (len(nums)+1)
# for num in nums:
#     if num > len(nums) or num < 1:
#         continue
#     Seen[num] = True
# for i in range(1, len(Seen)):
#     if not Seen[i]:
#         print i
#         exit()
# print len(Seen)
