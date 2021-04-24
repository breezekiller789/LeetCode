#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/plus-one-linked-list/

# 1. Reverse linked list
# 2. Add 1 to head, if carry needed, carry it until the end
# 3. Reverse linked list

# =========Code==========


class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


def Reverse(head):
    p = head.next
    q = head
    r = None
    while p:
        q.next = r
        r = q
        q = p
        p = p.next
    q.next = r
    return q


def Print_List(head):
    tmp = head
    while tmp:
        print tmp.val
        tmp = tmp.next


def Add_One(head):
    tmp = head
    carry_in = (tmp.val+1) // 10
    tmp.val = (tmp.val+1) % 10
    prev = tmp  # Keep track of previous node cuz we might need to add new node
    tmp = tmp.next
    while carry_in and tmp:
        prev = tmp
        # Added this cuz we face Read After Write problem, so we need to temp
        # this variable
        prev_val = tmp.val
        tmp.val = (prev_val+carry_in) % 10
        carry_in = (prev_val+carry_in)//10
        tmp = tmp.next
    # Deal with cases like 9999 + 1, there will be all zeros, but still carry a
    # carry_in, this if statement covers this cases
    if carry_in == 1:
        prev.next = ListNode(1)

    return head


head = ListNode(9)
head.next = ListNode(9)
head.next.next = ListNode(9)
head.next.next.next = ListNode(9)
head.next.next.next.next = ListNode(9)

head = Reverse(head)
head = Add_One(head)
Print_List(Reverse(head))
