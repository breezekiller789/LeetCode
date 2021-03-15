#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/add-two-numbers/
# 學習用python寫linked list，方便許多QQ，概念不難，程式碼的部分問題比較多，那個
# 生測資的動作真的太醜了，慢慢習慣一下:(，概念其實就是一個個去加，阿要小心進位
# ，如果進到最後carry還等於1，代表還要再生一個節點出來放carry，大致這樣。


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 生測資，很醜我知道，我會練一下
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)
l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

l3 = ListNode()     # linked list的head，這是一個dummy head
carry = 0
while l1 and l2:
    # 把值加起來，要記得有carry
    val = l1.val + l2.val + carry
    # 大於10就要進位，carry = 1，val要記得減掉10
    if val >= 10:
        carry = 1
        val -= 10
    else:
        carry = 0

    # 到這裡就是要insert了，是insert at tail
    new_Node = ListNode(val)
    tmp = l3
    while tmp.next:         # 走到linked list尾巴
        tmp = tmp.next
    tmp.next = new_Node     # insert!
    l1 = l1.next            # l1, l2往下一個節點移動
    l2 = l2.next            # l1, l2往下一個節點移動

# l1可能比較長，就要把剩下的也算進去，原理都一樣
while l1:
    val = l1.val + carry
    if val >= 10:
        carry = 1
        val -= 10
    else:
        carry = 0
    new_Node = ListNode(val)
    tmp = l3
    while tmp.next:
        tmp = tmp.next
    tmp.next = new_Node
    l1 = l1.next

# l2可能比較長，就要把剩下的也算進去，原理都一樣
while l2:
    val = l2.val + carry
    if val >= 10:
        carry = 1
        val -= 10
    else:
        carry = 0
    new_Node = ListNode(val)
    tmp = l3
    while tmp.next:
        tmp = tmp.next
    tmp.next = new_Node
    l2 = l2.next

# 到這邊，還是有可能有進位問題，例如999+1，最後第四位數會有一個carry要加進去
if carry == 1:
    new_Node = ListNode(carry)
    tmp = l3
    while tmp.next:
        tmp = tmp.next
    tmp.next = new_Node

l3 = l3.next    # dummy head不要，從下一個開始拿
tmp = l3
while tmp:
    print tmp.val
    tmp = tmp.next
