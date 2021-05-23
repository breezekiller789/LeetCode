#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/car-fleet/

# 這一題就是用sorting，但是還是有一點小巧思在裡面，我們先把位置跟速度都包起來，
# 用zip，然後用位置來排序，然後算出每一輛車到達終點所需要的時間，然後我們再走一
# 次時間陣列，如果發現現在時間比前面的最大時間相比，現在比較小，那就不用增加
# car fleet，因為我們不能超過在我們前面的車，我雖然速度比前面快，但是我不能超車
# ，題目規定的，所以就不用增加car fleet，反之，如果我比前面的車還要慢到終點，那
# 就是要增加car fleet了。


class Solution(object):
    def __init__(self):
        self.haha = 0

    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        self.haha = 0
        if not position or not speed:
            return 0
        times = [float(target-pos) / spd
                 for pos, spd in sorted(zip(position, speed), reverse=1)]
        leftUpperBound = times[0]
        carFleet = 1
        for i, time in enumerate(times[1:], start=1):
            # 我到終點所需時間比前面的還要久，代表我們是分道揚鑣，所以car fleet
            # 就要加一
            if time > times[i-1] and time > leftUpperBound:
                leftUpperBound = time
                carFleet += 1
        return carFleet


obj = Solution()
print obj.carFleet(10, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
