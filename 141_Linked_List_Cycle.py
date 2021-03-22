#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/linked-list-cycle/


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

Seen = set()
tmp = head
while tmp:
    if tmp.next in Seen:
        print "True"
        exit()
    else:
        Seen.add(tmp)
    tmp = tmp.next
print "False"
