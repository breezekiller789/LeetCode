#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/flatten-nested-list-iterator/

# 用遞迴解


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than
#        a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds
#        a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a
#        nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.allElement = []

        def Recursion(myList):
            tmpList = []
            for nested in myList:
                if not nested.isInteger():
                    tmpList.extend(Recursion(nested.getList()))
                else:
                    tmpList.append(nested.getInteger())
            return tmpList
        self.allElement = Recursion(nestedList)
        self.pointer = 0
        self.length = len(self.allElement)

    def next(self):
        """
        :rtype: int
        """
        ret = self.allElement[self.pointer]
        self.pointer += 1
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pointer != self.length
