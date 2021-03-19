#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/palindrome-linked-list/

# 我的作法比較直覺，就走一次linked list，然後走過每個節點就加進string字串，然後
# 再去判斷string是不是迴文，這樣就結束。
# Time = O(n)
# Space = O(n)


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


def Is_Palindrome(string, length):
    # 偶數長度跟奇數長度分開處理。
    if length % 2 == 0:
        # 前面一半跟後面一半比較
        return string[:length/2] == (string[length/2:])[::-1]
    else:
        return string[:length/2] == (string[length/2+1:])[::-1]


head = None
try:
    while 1:
        val = input()
        List_Insert(val)
        print "Insert {}".format(val)
except EOFError:
    pass
string = ""         # 待會要記錄linked list的節點
length = 0          # 走一次順便算長度
tmp = head.next     # 略過dummy head
while tmp:
    string += str(tmp.val)
    tmp = tmp.next
    length += 1
print Is_Palindrome(string, length)
