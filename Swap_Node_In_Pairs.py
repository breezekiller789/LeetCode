#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/swap-nodes-in-pairs/

# 挺簡單的，就是兩個節點值互換，跳兩個，主要就是一些邊界的檢查而已。


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 自己生測資 1->2->3->4，滿醜的:(
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

tmp = head
# 必須要多檢查tmp.next是不是有東西，如果tmp.next空的，代表這就是最後一個節點
# 不用做了，因為沒有下一個節點可以交換值
while tmp and tmp.next:
    # Swap function三步驟
    Tmp = tmp.val
    tmp.val = tmp.next.val
    tmp.next.val = Tmp
    # 跳兩個節點
    tmp = tmp.next.next
tmp = head
while tmp:
    print tmp.val
    tmp = tmp.next
