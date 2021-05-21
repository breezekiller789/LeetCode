#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

# Output: [2,1,1,0]
nums = [5, 2, 6, 1]

# Output: [0]
# nums = [-1]

# Output: [0,0]
# nums = [-1, -1]

# Output: [2,0,0]
# nums = [2, 0, 1]

# nums = [1, 0, 0, 0, 0, 0]


def BinarySearchAndInsert(nums, target, Result, sortedList):
    low = 0
    length = len(sortedList)
    high = length - 1
    mid = (low+high) / 2
    while low <= high:
        mid = (low+high) / 2
        if sortedList[mid] > target:
            high = mid - 1
        elif sortedList[mid] < target:
            low = mid + 1
        else:
            sortedList.insert(mid, sortedList[mid])
            while mid > 0 and mid < length and sortedList[mid] == target:
                mid -= 1
            return mid
    if sortedList[mid] > target:
        sortedList.insert(mid, target)
        return mid
    elif sortedList[mid] == target:
        sortedList.insert(mid, target)
        while mid > 0 and mid < length and sortedList[mid] == target:
            mid -= 1
        return mid
    else:
        sortedList.insert(mid+1, target)
        return mid+1


sortedList = []
Result = [0] * len(nums)
sortedList.append(nums[-1])
for i in xrange(len(nums)-2, -1, -1):
    Count = BinarySearchAndInsert(nums, nums[i], Result, sortedList)
    Result[i] = Count
print Result
