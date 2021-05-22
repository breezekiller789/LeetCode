#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/lru-cache/


class ListNode(object):
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.left = None
        self.right = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.DH = ListNode(None, None)    # Dummy head
        self.DT = ListNode(None, None)    # Dummy tail
        self.DH.right = self.DT
        self.DT.left = self.DH
        self.size = 0
        self.hashTable = dict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hashTable:
            return -1
        self.updateToTheTop(key)
        return (self.hashTable[key]).val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        # Key already exists
        if key in self.hashTable:
            (self.hashTable[key]).val = value
            self.updateToTheTop(key)
            return

        if self.size == self.capacity:
            # Cache full, evict LRU node
            self.evictAndUpdate(key, value)
            return

        # At least one capacity left, insert diretly
        newNode = ListNode(key, value)
        self.hashTable[key] = newNode
        newNode.left = self.DH
        newNode.right = self.DH.right
        self.DH.right = newNode
        newNode.right.left = newNode
        self.size += 1

    def evictAndUpdate(self, key, value):
        # Remove the node before DT
        target = self.DT.left
        target.left.right = self.DT
        self.DT.left = target.left
        del self.hashTable[target.key]
        del target

        newNode = ListNode(key, value)
        self.hashTable[key] = newNode
        newNode.left = self.DH
        newNode.right = self.DH.right
        self.DH.right = newNode
        newNode.right.left = newNode
        return

    def updateToTheTop(self, key):
        target = self.hashTable[key]

        # Remove the target
        target.left.right = target.right
        target.right.left = target.left

        # Insert into the front
        target.left = self.DH
        target.right = self.DH.right
        self.DH.right = target
        target.right.left = target
        return


obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
obj.put(3, 3)
obj.put(4, 4)
obj.put(5, 5)
print obj.get(1)
print obj.get(2)
print obj.get(3)
print obj.get(4)
