#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/top-k-frequent-elements/

nums = [1, 1, 1, 2, 2, 3]
k = 2


class Solution(object):
    def __init__(self):
        self.haha = 0

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        self.haha = 0
        hashTable = dict()
        for num in nums:
            if num not in hashTable:
                hashTable[num] = 1
            else:
                hashTable[num] += 1
        extractedList = hashTable.items()
        extractedList.sort(key=lambda x: x[1], reverse=1)
        result = []
        for element in extractedList[:k]:
            result.append(element[0])
        return result


obj = Solution()
print obj.topKFrequent(nums, k)
