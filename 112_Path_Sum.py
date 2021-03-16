#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/path-sum/

# 我就是用inorder下去走，每走一個節點，就加上該節點的值，然後如果該節點準備回去
# 之後，就扣回去，然後要小心，因為題目是規定root->leaf的長度，不是隨時命中target
# 就可以結束，題目要看清楚。


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def Inorder(root):
    global Sum
    global res
    # Base Condition
    if not root:
        return
    Sum += root.val
    # 命中，而且該節點是leaf，所以左右子點必須要是空
    if Sum == targetSum and not root.left and not root.right:
        res = True
    Inorder(root.left)
    Inorder(root.right)
    Sum -= root.val


targetSum = 22
Sum = 0
res = False
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

Inorder(root)
print res
