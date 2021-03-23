#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# 一開始覺得很難，但是回來寫一下就寫出來了，其實用inorder下去走一次就好了，原本
# 是在中間印東西，現在變成設定一個Count，就加一，因為BST inorder走出來就是排序好
# 的，所以就用Count去追蹤現在走到第幾小的，一旦跟k一樣，就可以結束了。

k = 4

# =======Code Starts========


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def Inorder(root):
    global Count
    if not root:
        return
    Inorder(root.left)
    Count += 1
    if Count == k:
        print root.val
        exit()
    Inorder(root.right)


# 測資
#          3
#       1    4
#     0   2    5
root = TreeNode(3)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right = TreeNode(4)
root.right.right = TreeNode(5)

Count = 0
Inorder(root)
