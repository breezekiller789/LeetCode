#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/remove-linked-list-elements/

# 1. check if head has next node, if no, then check if head is val directly,
# else go to 2.
# 2. make prev = head and rear = head.next, then go to while loop
# 3. if rear.val == val, prev.next = rear.next, delete rear, rear = prev.next

# ==============Code===============


class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


head = ListNode(6)
head.next = ListNode(6)
head.next.next = ListNode(6)
head.next.next.next = ListNode(6)
head.next.next.next.next = ListNode(6)
head.next.next.next.next.next = ListNode(6)

val = 6

if not head.next:
    if head.val == val:
        print "head is null"

prev = head
rear = head.next
while rear:
    if rear.val == val:
        prev.next = rear.next
        del rear
        rear = prev.next
    else:
        prev = rear
        rear = rear.next

if head.val == val:
    head = head.next

tmp = head
while tmp:
    print tmp.val
    tmp = tmp.next
