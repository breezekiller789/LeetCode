#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/intersection-of-two-linked-lists/


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 生測資
headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = ListNode(3)
headA.next.next.next = ListNode(4)

headB = ListNode(9)
headB.next = headA.next.next


# Hashing
Seen = set()
tmp = headA
while tmp:
    Seen.add(tmp)
    tmp = tmp.next
tmp = headB
while tmp:
    if tmp in Seen:
        print tmp.val
        break
    tmp = tmp.next
