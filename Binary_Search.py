#!/usr/bin/env python3
# -*- coding: utf-8 -*-

nums = [i for i in range(20)]

target = 0
low = 0
high = len(nums)-1
while low <= high:
    mid = (low+high)//2
    if nums[mid] == target:
        print "Found it at {}".format(mid)
        exit()
    elif nums[mid] > target:
        high = mid - 1
    elif nums[mid] < target:
        low = mid + 1
