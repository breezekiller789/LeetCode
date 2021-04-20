#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/delete-nodes-and-return-forest/


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    global Nodes
    if not root:
        return
    inorder(root.left)
    Nodes.append(root)
    # print root.val
    inorder(root.right)


def Level_Order(root, to_delete):
    Q = []
    Q.append(root)
    current = 1
    Total = 1
    tmp = Q[current]
    while current <= Total:
        # if tmp in to_delete:
        #     tmp = Q[current]
        #     current += 1
        #     continue
        if tmp.left:
            Total += 1
            Q.append(tmp.left)
            # if tmp.left in to_delete:
            #     tmp.left = None
        if tmp.right:
            Total += 1
            Q.append(tmp.right)
            # if tmp.right in to_delete:
            #     tmp.right = None
        tmp = Q[current]
        current += 1
    return Q


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
to_delete = [root.right, root.left.right]
Q = Level_Order(root, to_delete)
for i in Q:
    print i.val
# inorder(root)
