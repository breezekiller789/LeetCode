#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/advantage-shuffle/

# 1. Sort nums1
# 2. Use the snail crawling method


# Output: [2,11,7,15]
nums1 = [2, 7, 11, 15]
nums2 = [1, 10, 4, 11]

# Output: [24,32,8,12]
# [8, 12, 24, 32]
# nums1 = [12, 24, 8, 32]
# nums2 = [13, 25, 32, 11]

nums1.sort()
length = len(nums1)
taken = [False for _ in range(length)]
result = [None for _ in range(length)]
if nums2[0] < nums1[0]:
    result[0] = nums1[0]
    taken[0] = True
for i, num in enumerate(nums2):
    snailPosition = 1
    while snailPosition < length and num >= nums1[snailPosition]:
        snailPosition *= 2
    if snailPosition >= length:
        snailPosition /= 2
        while snailPosition < length and num >= nums1[snailPosition]:
            snailPosition += 1
        if snailPosition >= length:
            for idx, istaken in enumerate(taken):
                if not istaken:
                    result[i] = nums1[idx]
                    taken[idx] = True
                    break
        else:
            result[i] = nums1[snailPosition]
            taken[snailPosition] = True
    elif num < nums1[snailPosition] and not result[i]:
        result[i] = nums1[snailPosition]
        taken[snailPosition] = True
print result
