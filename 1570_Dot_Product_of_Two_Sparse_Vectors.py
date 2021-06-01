#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

# Hashing

# Output: 8
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
nums1 = [1, 0, 0, 2, 3]
nums2 = [0, 3, 0, 4, 0]

# Output: 0
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
nums1 = [0, 1, 0, 0, 0]
nums2 = [0, 0, 0, 0, 2]

# Output: 6
nums1 = [0, 1, 0, 0, 2, 0, 0]
nums2 = [1, 0, 0, 0, 3, 0, 4]


class SparseVector(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.hashTable = dict()
        for i, num in enumerate(nums):
            if num != 0:
                self.hashTable[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        Sum = 0
        for index in self.hashTable:
            if index not in vec.hashTable:
                continue
            else:
                Sum += self.hashTable[index] * vec.hashTable[index]
        return Sum


v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
ans = v1.dotProduct(v2)
print ans
