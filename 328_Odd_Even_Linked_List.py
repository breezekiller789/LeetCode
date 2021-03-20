#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/odd-even-linked-list/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def List_Insert(val):
    global head
    global prev
    if not head:
        head = ListNode(val)
        prev = head
    prev.next = ListNode(val)
    prev = prev.next


def Grouping():
    global Odd_Head
    global Even_Head
    Round = 1                   # 來看現在是在奇數還是在偶數。
    tmp_head = head             # 來走一次完整的linked list
    Prev_Odd = Odd_Head         # 因為要一直insert，所以要記錄previous node
    Prev_Even = Even_Head       # 因為要一直insert，所以要記錄previous node
    while tmp_head:
        if Round % 2 == 0:      # 偶數會進來。
            if not Prev_Even:   # 一開始的偶數頭一定會是空，因為初始化給他空。
                Even_Head = ListNode(tmp_head.val)
                Prev_Even = Even_Head
            Prev_Even.next = ListNode(tmp_head.val)     # 每次就是insert然後移動
            Prev_Even = Prev_Even.next                  # previous
        else:                   # 奇數會進來。
            if not Prev_Odd:    # 一開始一樣，奇數頭一定也是空。
                Odd_Head = ListNode(tmp_head.val)
                Prev_Odd = Odd_Head
            Prev_Odd.next = ListNode(tmp_head.val)      # 每次就是insert然後移
            Prev_Odd = Prev_Odd.next                    # previous

        tmp_head = tmp_head.next    # 下一個iteration
        Round += 1                  # Round+1


def Print_List(head):
    tmp = head
    while tmp:
        print tmp.val
        tmp = tmp.next


head = None
try:
    while 1:
        val = input()
        List_Insert(val)
        print "Insert {}".format(val)
except EOFError:
    pass

head = head.next    # skip dummy head

# ======================Code Starts======================

if not head or not head.next or not head.next.next:
    print "Only Two Nodes!"

Odd_Head = None
Even_Head = None

Grouping()      # 做Grouping，奇偶數分開。

Odd_Head = Odd_Head.next        # skip dummy head
Even_Head = Even_Head.next      # skip dummy head

tmp = Odd_Head.next             # 要進去把Even接在Odd屁股後面。
while tmp.next:
    tmp = tmp.next
tmp.next = Even_Head

Print_List(Odd_Head)
