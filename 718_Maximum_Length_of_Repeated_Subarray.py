#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/maximum-length-of-repeated-subarray/


# DP approach, dp[i][j] means the maximum same subarray in nums1[i:] and
# nums2[j:], i and j goes backwards. After it is all done, we have to get the
# maximum from dp array, row by row


nums1 = [1, 2, 3, 2, 1]
nums2 = [3, 2, 1, 4, 7]
# nums1 = [0, 0, 0, 0, 0]
# nums2 = [0, 0, 0, 0, 0]
# nums1 = [0, 1, 1, 1, 1]
# nums2 = [1, 0, 1, 0, 1]
nums1 = [0, 0, 0, 0, 1]
nums2 = [1, 0, 0, 0, 0]


s1Length = len(nums1)
s2Length = len(nums2)
dp = [[0 for _ in range(s2Length+1)] for _ in range(s1Length+1)]
for i in xrange(s1Length-1, -1, -1):
    for j in xrange(s2Length-1, -1, -1):
        if nums1[i] == nums2[j]:
            dp[i][j] = dp[i+1][j+1] + 1
print max(max(row) for row in dp)


# Hashing got TLE
# hashTable1 = set()
# s1Length = len(nums1)
# s2Length = len(nums2)

# for i in range(s1Length):
#     for j in range(i+1, s1Length+1):
#         hashTable1.add(tuple(nums1[i:j]))
# Max = 0
# for i in range(s2Length):
#     for j in range(i+1, s2Length+1):
#         key = tuple(nums2[i:j])
#         if key in hashTable1:
#             Max = max(Max, len(key))
# print Max
