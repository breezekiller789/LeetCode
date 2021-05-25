#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
# https://leetcode.com/problems/sliding-window-maximum/

# 參考解答：https://www.youtube.com/watch?v=DfljaUwZsOk

# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 2


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 記得我們dequeue裡面放的東西是index，不是value
        Q = collections.deque()
        output = []
        left, right = 0, 0
        while right < len(nums):

            # Pop the queue from right side until the top element is greater
            # than new number
            while Q and nums[Q[-1]] < nums[right]:
                Q.pop()

            # Now we can savely add our new index
            Q.append(right)

            # Remove left element from Queue as we move our sliding window
            # forward
            if left > Q[0]:
                Q.popleft()

            # when the sliding window fully expanded, we wanna move our left
            # pointer and add the maximum to our output array
            if right+1 >= k:
                output.append(nums[Q[0]])
                left += 1
            # right pointer always goes forward
            right += 1
        return output


obj = Solution()
print obj.maxSlidingWindow(nums, k)

# 我的原始想法，是可以work的，但是TLE，最差情況就是那種一直遞減的情況，因為這樣
# 我就必須要每一次都重新下去找max，很浪費時間，最差還是O(nk)
# left = 0
# right = k-1
# Max = [float("-inf"), 0]
# for i, num in enumerate(nums[left:right+1], start=0):
#     if num > Max[0]:
#         Max = [num, i]
# result = []
# result.append(Max[0])
# while right < len(nums)-1:
#     left += 1
#     right += 1
#     if nums[right] > Max[0]:
#         Max = [nums[right], right]

#     if left > Max[1]:
#         Max = [float("-inf"), left]
#         for i, num in enumerate(nums[left:right+1], start=left):
#             if num > Max[0]:
#                 Max = [num, i]
#     result.append(Max[0])
# print result
