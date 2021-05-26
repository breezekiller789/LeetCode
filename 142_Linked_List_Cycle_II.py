#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/linked-list-cycle-ii/

# Floyd's tortoise and hare method


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self):
        self.haha = 0

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.haha = 0
        # Floyd's tortoise and hare method
        if not head:
            return
        tortoise = head
        hare = head
        while True:
            if not tortoise or not hare or not tortoise.next or not hare.next:
                return
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                break
        tortoise = head
        while True:
            if tortoise == hare:
                return tortoise
            tortoise = tortoise.next
            hare = hare.next


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
obj = Solution()
obj.detectCycle(head)
