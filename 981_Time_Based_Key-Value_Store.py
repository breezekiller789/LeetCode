#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict

# https://leetcode.com/problems/time-based-key-value-store/

# Binary search，因為題目有說timestamp一定是遞增在insert，所以才可以用binary
# search，還有用hashing


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashTable = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.hashTable[key].append([timestamp, value])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        array = self.hashTable[key]
        low = 0
        high = len(array)-1
        while low <= high:
            mid = (low+high) / 2
            if array[mid][0] > timestamp:
                high = mid - 1
            elif array[mid][0] < timestamp:
                low = mid + 1
            else:
                return array[mid][1]
        return array[low-1][1] if low != 0 else ""


obj = TimeMap()
obj.set("foo", "bar", 1)
obj.set("foo", "bar2", 2)
obj.set("foo", "bar4", 4)
obj.set("foo", "bar8", 8)
print obj.get("foo", 0)
