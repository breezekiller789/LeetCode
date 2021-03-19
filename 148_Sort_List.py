#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/reverse-linked-list/

# 我就用直覺的作法，走一次linked list然後放進一個array list，排序array list，然
# 後再放回去原本的linked list


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


head = None

# insert一些測資，輸入一些整數
try:
    while 1:
        val = input()
        List_Insert(val)
        print "Insert {}".format(val)
except EOFError:
    pass

nums = []
tmp = head.next                 # 略過dummy head
while tmp:
    nums.append(tmp.val)        # 走一次linked list，把東西都拿出來，放nums
    tmp = tmp.next

nums = sorted(nums, reverse=1)  # 排序，由大->小，因為待會我要用pop的方式拿

tmp = head.next                 # 略dummy head
while tmp:
    tmp.val = nums.pop()        # 一個個放回去原本linked list中
    tmp = tmp.next

# 印結果
# # ========================
# tmp = head.next
# while tmp:
#     print tmp.val
#     tmp = tmp.next
