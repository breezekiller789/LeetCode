#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/design-linked-list/


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index > self.size:
            return -1
        tmp = self.head
        while tmp and index > 0:
            tmp = tmp.next
            index -= 1
        return tmp.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        newNode.next = self.head.next
        self.head = newNode
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        tmp = self.head
        prev = tpm
        while index > 0:
            index -= 1
            prev = tmp
            tmp = tmp.next
        newNode = Node(val)
        newNode.next = tmp
        prev.next = newNode
        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
        if index == 0:
            tmp = self.head
            self.head = self.head.next
            del tmp
        tmp = self.head
        prev = tmp
        while index > 0:
            index -= 1
            prev = tmp
            tmp = tmp.next
        prev.next = tmp.next
        del tmp



obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtHead(5)
obj.addAtHead(11)
obj.addAtHead(7)
obj.addAtHead(8)
