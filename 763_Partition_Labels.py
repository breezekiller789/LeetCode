#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict

# https://leetcode.com/problems/partition-labels/

# 方法就是先算出每個字元的起始跟終點位置，這樣我們就知道每一個字元出現的區間，
# 有了區間我們再apply之前的merge interval我們就可以做出我們要的partition效果，但
# 是要記得要排序。

# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits s into less parts.
s = "ababcbacadefegdehijhklij"

startAndEndPosition = defaultdict(list)
# 先算出每一個字元的起始位置跟最後位置。
for i, char in enumerate(s):
    if char not in startAndEndPosition:
        startAndEndPosition[char] = [i, i]
    else:
        startAndEndPosition[char][1] = i

intervals = startAndEndPosition.values()
intervals.sort()        # 要先排序

# 開始merge interval
mergedInterval = []
for interval in intervals:
    if not mergedInterval or interval[0] > mergedInterval[-1][-1]:
        mergedInterval.append(interval)
    else:
        mergedInterval[-1] = ([mergedInterval[-1][0],
                               max(mergedInterval[-1][-1], interval[-1])])

# 再用merge過後的區間，算每一個區間的距離
Ans = []
for interval in mergedInterval:
    Ans.append(interval[-1] - interval[0] + 1)
print Ans
