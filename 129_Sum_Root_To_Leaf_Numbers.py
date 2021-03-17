#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# 我就呼叫inorder traversal，每走一個節點就append直到遇到leaf，就算Sum，
# 跟112 path sum一樣想法


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def Inorder(root):
    global String
    global Sum
    if not root:
        return
    String += str(root.val)     # 走一個節點就append一個
    if not root.left and not root.right:    # 會進去代表走到leaf
        Sum += int(String)
    Inorder(root.left)
    Inorder(root.right)
    String = String[:-1]        # 這個節點準備要return了，把最後一個字元抽掉


#       3
#    9     2
#        1   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(2)
root.right.left = TreeNode(1)
root.right.right = TreeNode(7)
String = ""
Sum = 0
Inorder(root)
print Sum
