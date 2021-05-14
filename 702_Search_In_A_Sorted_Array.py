#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

# 這一題基本上就是Binary search但是比較不一樣，類似烏龜爬行法，因為我們不知道陣
# 列大小，所以我們一開始要用烏龜爬行法，往前爬，直到爬到越界或者爬超過目標為止。


class ArrayReader(object):
    def get(self, index):
        """
        :type index: int
        :rtype int
        """
        # 隨便寫一下
        return self


reader = ArrayReader()
target = 5
current = 0
# 從零開始爬，直到爬到越界或者爬超過目標為止。
while reader.get(current) != 2147483647 and reader.get(current) < target:
    if current == 0:
        current += 1
    current *= 2

# 直接中獎，回傳
if reader.get(current) == target:
    print current
# 走到這邊就知道upper bound了，這時候就是binary search
else:
    low = current/2
    high = current
    while low <= high:
        mid = (low+high)/2
        if reader.get(mid) < target:
            low = mid+1
        elif reader.get(mid) > target:
            high = mid-1
        else:
            print mid
            exit()
    print -1
