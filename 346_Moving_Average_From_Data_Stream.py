#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/moving-average-from-data-stream/

# 不難


class MovingAverage(object):

    def __init__(self, size):
        self.size = size
        self.Avgs = []
        self.count = 0

    def next(self, val):
        if self.count < self.size:
            self.count += 1
            self.Avgs.append(val)
            return float(sum(self.Avgs))/self.count
        else:
            del self.Avgs[0]
            self.Avgs.append(val)
            return float(sum(self.Avgs))/self.count


obj = MovingAverage(4)
print obj.next(2)
print obj.next(4)
print obj.next(5)
print obj.next(10)
print obj.next(11)
