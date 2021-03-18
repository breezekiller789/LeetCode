#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def List_Insert(head, num):
    tmp = head
    while tmp.next:
        tmp = tmp.next
    # print "Insert {}".format(num)
    tmp.next = ListNode(num)


head = ListNode()
try:
    while 1:
        num = input()
        List_Insert(head, num)
except EOFError:
    pass

# tmp = head.next
# while tmp:
#     print tmp.val
#     tmp = tmp.next

n = 1
Previous = []

# 如果n == 1代表就是把尾巴去掉
if n == 1:
    if not head.next.next:
        print []
        exit()
    tmp = head
    while tmp.next.next:
        tmp = tmp.next
    del tmp.next
    exit()

head = head.next            # 略過dummy head

i, tmp = 0, head
while i <= n and tmp:
    Previous.append(tmp)
    tmp = tmp.next
    i += 1
if not tmp:
    print head.next.val
    exit()

# for i in range(n+1):        # 存n+1個節點，因為要刪除第n個，必須要記錄上一個
#     Previous.append(tmp)
#     tmp = tmp.next

# 走到這裡Previous就裝滿了n+1個節點了，可以開始從頭往下
tmp = head
while tmp:
    Previous.append(tmp)        # 當遇到新的就新增上去
    del Previous[0]             # 然後把最前面的刪掉
    tmp = tmp.next

Previous[0].next = Previous[1].next     # 這兩步就是在做刪除的動作
del Previous[1]

tmp = head
while tmp:
    print tmp.val
    tmp = tmp.next
