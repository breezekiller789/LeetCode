#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Output: 2.00000
nums1 = [1,3]
nums2 = [2]

# Output: 2.50000
nums1 = [1,2]
nums2 = [3,4]

# Output: 0.00000
nums1 = [0,0]
nums2 = [0,0]

# Output: 1.00000
# nums1 = []
# nums2 = [1]

# Output: 2.00000
# nums1 = [2]
# nums2 = []


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def Median(input1, input2):
            x = len(input1)
            y = len(input2)
            if x > y:
                return Median(input2, input1)
            low = 0
            high = x
            while low <= high:
                partitionX = (low+high)/2
                partitionY = (x+y+1)/2 - partitionX

                if partitionX == 0:
                    LeftX = float("-inf")
                else:
                    LeftX = input1[partitionX-1]

                if partitionX == x:
                    RightX = float("inf")
                else:
                    RightX = input1[partitionX]

                if partitionY == 0:
                    LeftY = float("-inf")
                else:
                    LeftY = input2[partitionY-1]

                if partitionY == y:
                    RightY = float("inf")
                else:
                    RightY = input2[partitionY]

                if LeftX < RightY and LeftY < RightX:
                    if (x+y) % 2 == 0:
                        return float(max(LeftX, LeftY) + min(RightX, RightY))/2
                    else:
                        return max(LeftX, LeftY)
                elif LeftX > RightY:
                    high = partitionX-1
                else:
                    low = partitionX+1
        return Median(nums1, nums2)
obj = Solution()
print obj.findMedianSortedArrays(nums1, nums2)
