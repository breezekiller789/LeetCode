#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# 就是double pointer的概念，一個指著前面，一個指著後面，如果兩者一樣，後者刪掉
# 然後後者往後移動一格


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
Seen = []

Seen.append(head.val)   # 先把第一個加進去，這樣一開始才會知道有沒有重複
cur = head.next         # cur指著後面
prev = head             # prev指著前面
while cur:
    # 如果還沒有出現在Seen代表還沒看過，先加進去，然後prev, cur都一起往後
    if cur.val not in Seen:
        Seen.append(cur.val)
        prev = cur
        cur = cur.next
    # 會進來這裡，代表prev, cur兩個一樣，這時候就是要刪除節點，步驟不可以換
    else:
        next_Node = cur.next    # 要先把下一個記下來，不然刪掉就整條沒了
        del cur                 # 刪掉cur
        prev.next = next_Node   # 把prev接上去
        cur = prev.next         # cur往後
tmp = head
while tmp:
    print tmp.val
    tmp = tmp.next
