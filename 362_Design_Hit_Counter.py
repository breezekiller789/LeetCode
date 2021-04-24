#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/design-hit-counter/


class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Hits_Timestamp = []
        self.HitCount = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        self.Hits_Timestamp.append(timestamp)
        self.HitCount += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        Start = timestamp-300
        Count = 0
        if Start < 0:
            Start = 0
        for _ in self.Hits_Timestamp:
            if _ <= timestamp and _ > Start:
                Count += 1
        return Count


Hit = HitCounter()
Hit.hit(1)
Hit.hit(2)
Hit.hit(2)
Hit.hit(2)
Hit.hit(2)
Hit.hit(4)
Hit.hit(8)
Hit.hit(300)
Hit.hit(301)
Hit.hit(301)
Hit.hit(500)
print Hit.getHits(500)
