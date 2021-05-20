#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# 我覺得這一題沒有定義好題目，path的定義是什麼模糊不清，就做到這樣了，我大部分會
# 對，但是如果遇到像是[2, -1]，這樣就會錯，答案是要2，我會印1，因為我是bottum-up
# 不過沒關係，對於遞迴又更有印象。


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def Preorder(root):
    global Max
    if not root:
        return 0
    leftPath = max(0, Preorder(root.left))
    rightPath = max(0, Preorder(root.right))
    currentPath = root.val + leftPath + rightPath
    Max = max(Max, currentPath)
    return root.val + max(leftPath, rightPath)


root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
Max = float("-inf")
print Preorder(root)
