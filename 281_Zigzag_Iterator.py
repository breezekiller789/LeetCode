#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/zigzag-iterator/

# 1. Simply add two pointers, one point to v1, one point to v2, as user get one
# element, move the extracted pointer forward, also keep a variable called
# round, to keep track of user's action, just mod it to see what round is it
# right now, is it even round or odd round, that's basicly it.


# =========Code=========


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1_Pointer = -1
        self.v2_Pointer = -1
        self.Vectors = [v1, v2]
        self.v1Length = len(v1)
        self.v2Length = len(v2)
        self.Round = 0

    def next(self):
        """
        :rtype: int
        """
        Round_Count = self.Round % 2
        self.Round += 1
        # To see what this round is, even or odd
        if Round_Count == 0:
            # if v1 still has elements to get, get it straight away
            if self.v1_Pointer+1 < self.v1Length:
                self.v1_Pointer += 1
                return self.Vectors[Round_Count][self.v1_Pointer]
            # if v1 has no elements, change to v2
            else:
                self.v2_Pointer += 1
                return self.Vectors[Round_Count+1][self.v2_Pointer]

        else:
            # vise versa, just like v1, but opposite
            if self.v2_Pointer+1 < self.v2Length:
                self.v2_Pointer += 1
                return self.Vectors[Round_Count][self.v2_Pointer]
            else:
                self.v1_Pointer += 1
                return self.Vectors[Round_Count-1][self.v1_Pointer]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.Round < self.v1Length+self.v2Length


Z, v = ZigzagIterator([1, 2, 7, 7, 7, 7, 7], [3, 4, 5, 6]), []
while Z.hasNext():
    print Z.next()
