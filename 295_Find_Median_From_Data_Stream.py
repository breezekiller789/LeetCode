#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/find-median-from-data-stream/


class MedianFinder(object):
    def __init__(self):
        self.Nums = []
        self.length = 0

    def addNum(self, num):
        self.Nums.append(num)
        self.Nums = sorted(self.Nums)
        self.length += 1

    def findMedian(self):
        if (self.length+1) % 2 == 0:
            return self.Nums[(self.length)/2]
        else:
            return (float(self.Nums[self.length/2])
                    + float(self.Nums[self.length/2-1]))/2


M = MedianFinder()
M.addNum(30)
M.addNum(3)
M.addNum(4)
M.addNum(18)
M.addNum(20)
print M.findMedian()
