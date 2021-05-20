#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# 先走一次list，把每一個節點都放進一個list，最重要就是要做一些邊界檢查。


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def __init__(self):
        self.haha = 0

    def removeNthFromEnd(self, head, n):
        self.haha = None
        tmp = head
        allNodes = []
        while tmp:
            allNodes.append(tmp)
            tmp = tmp.next
        if len(allNodes) == 1:
            return None
        if len(allNodes) == n:
            return allNodes[0].next
        allNodes[-(n+1)].next = allNodes[-n].next
        return allNodes[0]


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
n = 2

obj = Solution()
result = obj.removeNthFromEnd(head, n)
tmp = result
while tmp:
    print tmp.val
    tmp = tmp.next
