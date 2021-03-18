#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/reverse-linked-list/

# 經典中的經典


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 我這個insert有用一個prev紀錄linked list尾巴，所以就直接insert在prev後面就好
def List_Insert(val):
    global head
    global prev
    if not head:
        head = ListNode(val)
        prev = head
    prev.next = ListNode(val)
    prev = prev.next


# 反轉linked list
def Invert(head):
    q = head
    p = head.next
    r = None
    while p:
        q.next = r
        r = q
        q = p
        p = p.next
    q.next = r
    return q


head = None
prev = None

# insert一些測資，輸入一些整數
try:
    while 1:
        val = input()
        List_Insert(val)
        print "Insert {}".format(val)
except EOFError:
    pass


head = Invert(head.next)

tmp = head
while tmp:
    print tmp.val
    tmp = tmp.next
