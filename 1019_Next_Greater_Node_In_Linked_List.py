#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/next-greater-node-in-linked-list/

# Ref Q.739


class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

nums = []
tmp = head
while tmp:
    nums.append(tmp.val)
    tmp = tmp.next
result = [0 for _ in range(len(nums))]
stack = []
for i, num in enumerate(nums):
    while stack and num > nums[stack[-1]]:
        result[stack.pop()] = num
    stack.append(i)
print result
