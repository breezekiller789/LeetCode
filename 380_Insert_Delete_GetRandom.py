#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

# https://leetcode.com/problems/insert-delete-getrandom-o1/

# Hashing


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Presents = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already
        contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.Presents:
            self.Presents.add(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the
        specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.Presents:
            self.Presents.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.sample(self.Presents, 1)[0]


obj = RandomizedSet()
obj.insert(1)
obj.insert(1)
obj.insert(2)
obj.insert(1)
obj.insert(5)
obj.insert(1)
print obj.getRandom()
