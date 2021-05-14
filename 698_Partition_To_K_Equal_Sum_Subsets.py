#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

# This question is so god damn hard... I still got TLE. I'm gonna stick with
# this solution...


def KEqualSumSubsets(nums, k, alreadyUsed, bucketSum, progressBucket,
                     iterationStart):
    if k == 1:
        return True
    if progressBucket == bucketSum:
        return KEqualSumSubsets(nums, k-1, alreadyUsed, bucketSum, 0, 0)
    for idx, num in enumerate(nums):
        if not alreadyUsed[idx]:
            alreadyUsed[idx] = True
            if KEqualSumSubsets(nums, k, alreadyUsed, bucketSum,
                                progressBucket+nums[idx], idx+1):
                return True
            alreadyUsed[idx] = False
    return False


# nums = [4, 3, 2, 3, 5, 2, 1]
# k = 4
# nums = [1, 2, 3, 4]
# k = 3
nums = [1, 1, 1, 1, 2, 2, 2, 2, 2]
k = 2

Sum = sum(nums)
if Sum % k != 0:
    print False
    exit()

bucketSum = Sum / k
length = len(nums)
alreadyUsed = [False for _ in range(length)]
print KEqualSumSubsets(nums, k, alreadyUsed, bucketSum, 0, 0)
