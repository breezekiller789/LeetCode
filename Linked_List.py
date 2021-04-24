#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Linked_List(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def Insert_Tail(self, val):
        new_Node = ListNode(val)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            self.tail = self.tail.next

    def Print_List(self):
        tmp = self.head
        while tmp:
            print tmp.val
            tmp = tmp.next


LL = Linked_List()
LL.Insert_Tail(1)
LL.Insert_Tail(2)
LL.Insert_Tail(3)
LL.Print_List()
