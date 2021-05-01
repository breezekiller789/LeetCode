#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

# 1. Inorder traversal
# 2. Insert in to double linked list

# ===========Code===========


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Insert(key, head):
    if not head:
        newNode = ListNode(key)
        head = newNode
        head.left = head
        head.right = head
    else:
        newNode = ListNode(key)
        tmp = head
        # Go to the end of linked list
        while tmp.right:
            # Enter this if statement if tmp.right is head
            if tmp.right == head:
                break
            tmp = tmp.right
        tmp.right = newNode     # point the tail to the new node
        newNode.left = tmp      # make the tail node as prev node of new node
        newNode.right = head    # make the list circular, tail point to head
        head.left = newNode     # make the list circular, head left point tail
    return head


def Inorder(root, head):
    if not root:
        return head
    head = Inorder(root.left, head)
    head = Insert(root.val, head)
    head = Inorder(root.right, head)
    return head


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
head = Inorder(root, None)
tmp = head
while tmp:
    print tmp.val
    tmp = tmp.right
    if tmp == head:
        break
