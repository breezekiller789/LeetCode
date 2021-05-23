#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/koko-eating-bananas/

# Binary search，low從1開始，high從香蕉中挑出最多香蕉的，為什麼是要挑出最多香蕉
# ，因為如果ｋ比最多香蕉還要多的話，其實沒有意義，因為k再多，最後還是只是piles的
# 長度而已，因為koko他就可以每一堆都吃光光，給最大就可以吃光了，還更大就沒有用意
# ，然而我們二分搜尋就是在這中間找k，每一次迭代我們都去算現在這個k值讓koko吃完須
# 要多久時間，如果要吃超過時間，那就增加k值，讓他吃快點，就把low往後移動，反之，
# 如果時間太充裕，讓他吃慢一點，就把high往前移動。


class Solution(object):
    def __init__(self):
        self.haha = 0

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        self.haha = 0

        def timeNeededToEat(piles, k):
            timeCount = 0
            for pile in piles:
                timeCount += pile/k
                if pile % k != 0:
                    timeCount += 1
            return timeCount
        low = 1
        high = max(piles)
        while low <= high:
            k = low + (high-low)/2
            Time = timeNeededToEat(piles, k)
            if Time > h:
                low = k + 1
            else:
                high = k - 1
        return low


obj = Solution()
print obj.minEatingSpeed([3, 6, 7, 11], 8)
