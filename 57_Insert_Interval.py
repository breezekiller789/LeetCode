#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/insert-interval/

# 1. Binary search，分別用newInterval的兩個值去做binary search，然後分別兩個會有
# 各自找到的位置，首先要檢查，如果兩個找到的位置一樣，代表什麼事都不用做。
# 如果位置不一樣，那就搜集兩個位置的區間，把他們給merge

# todo:
# 快寫完了但是還是有蟲，特別是在邊界的時候，像是下面這個[13, 18]的測資，他會超過
# ，要cover這種情況，然後還有就是完全落在邊界的情況，像是[20, 30]這種，完全落在外
# 面的，就這兩種情況還沒有cover到。

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
# newInterval = [13, 18]
# ==========Code Starts=========


intervals.append(newInterval)
intervals = sorted(intervals)
Ans = []
for idx, interval in enumerate(intervals):
    if not Ans or interval[0] > Ans[-1][-1]:
        Ans.append(interval)
    else:
        Ans[-1] = [Ans[-1][0], max(Ans[-1][-1], interval[1])]
print Ans


# Initial thoughts
# length = len(intervals)


# def is_Within_Interval(idx, val):
#     if val >= intervals[idx][0] and val <= intervals[idx][1]:
#         return True
#     return False


# def Bin_Search(offset, key):
#     low = 0
#     high = length - 1
#     while low <= high:
#         mid = (low+high)/2
#         # print low, mid, high
#         if intervals[mid][offset] >= key:
#             if is_Within_Interval(mid, key):
#                 return mid
#             high = mid - 1
#         elif intervals[mid][offset] <= key:
#             if is_Within_Interval(mid, key):
#                 return mid
#             low = mid + 1


# Left_Idx = Bin_Search(0, newInterval[0])
# Right_Idx = Bin_Search(1, newInterval[1])
# print Left_Idx, Right_Idx

# if Left_Idx == Right_Idx:
#     exit()

# Low_Bound = intervals[Left_Idx][0]
# Upper_Bound = intervals[Right_Idx][1]
# for idx in range(Left_Idx, Right_Idx+1):
#     del intervals[Left_Idx]
# intervals.insert(Left_Idx, [Low_Bound, Upper_Bound])
# print intervals
