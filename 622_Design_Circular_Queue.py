#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/design-circular-queue/


class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.Q = [None for _ in range(k+1)]
        self.rear = 0
        self.front = 0
        self.size = k+1

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.rear = (self.rear+1) % self.size
        self.Q[self.rear] = value
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.front = (self.front+1) % self.size
        self.Q[self.front] = None
        return True

    def Front(self):
        """
        return the element on the front pointer
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.Q[(self.front+1) % self.size]

    def Rear(self):
        """
        return the element on the rear pointer
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.Q[self.rear]

    def isEmpty(self):
        """
        :rtype: bool
        """
        size = (self.rear-self.front+self.size) % self.size
        return size == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return (self.rear+1) % self.size == self.front


obj = MyCircularQueue(3)
print obj.enQueue(1)
print obj.enQueue(2)
print obj.enQueue(3)
print obj.enQueue(4)
print obj.Rear()
print obj.isFull()
print obj.deQueue()
print obj.enQueue(4)
print obj.Rear()
