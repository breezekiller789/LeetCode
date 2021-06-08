#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# 這個top down evaluate binary的方法在Compiler的時候有教，超讚的，不然的話會超級
# 麻煩，因為要先反轉，然後在一個一個算。


class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)
head.next.next.next = ListNode(0)
head.next.next.next.next = ListNode(1)
tmp = head.next
result = head.val
while tmp:
    result *= 2
    result += tmp.val
    tmp = tmp.next
print result
