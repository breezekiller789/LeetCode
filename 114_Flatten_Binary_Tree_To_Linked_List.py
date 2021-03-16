#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# 這題卡好久，結果是回傳規格看錯，別再犯...，題目不難就是先preorder走一次，每
# 走一個就加進list，最後再按照list去造skew binary tree，沒啥難的。


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def Preorder(root):
    if not root:
        return
    print root.val
    # 每走一個節點就加進list
    Pre.append(root.val)

    Preorder(root.left)
    Preorder(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)

# 下次一定要記得cover這種base情況，如果傳空的進來，要先檢查
if not root:
    print []

head = TreeNode()
Pre = []

# 走一次preorder
Preorder(root)


tmp = root          # 因為要下去走迴圈所以要先assign
root.left = None    # 左邊要清成None
for i in Pre[1:]:
    new_Node = TreeNode(i)
    tmp.right = new_Node
    tmp = tmp.right
Preorder(root)
