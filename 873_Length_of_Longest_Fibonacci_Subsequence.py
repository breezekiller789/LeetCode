#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

# Output: 5
# Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
arr = [1, 2, 3, 4, 5, 6, 7, 8]

# Output: 3
# Explanation: The longest subsequence that is fibonacci-like:
# [1,11,12], [3,11,14] or [7,11,18]
# arr = [1, 3, 7, 11, 12, 14, 18]

# Output: 5
arr = [2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50]

# arr = [1,5,6,7,10,12,17,24,41,65]

maxLength = float("-inf")
length = len(arr)
for k in range(length-2):
    for i in range(k+1, length-1):
        tmpList = [arr[k], arr[i]]
        supposedToBe = tmpList[-1] + tmpList[-2]
        for j in range(i+1, length):
            if arr[j] == supposedToBe:
                tmpList.append(supposedToBe)
                maxLength = max(maxLength, len(tmpList))
                supposedToBe = tmpList[-1] + tmpList[-2]
            elif arr[j] > supposedToBe:
                break
        print tmpList
print maxLength
