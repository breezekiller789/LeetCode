#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# 原本這題以為要用queue來做，但是因為題目要的是同level要放同一個list，變成說我
# 要pass level資訊進去，所以用queue是沒辦法做的，阿這邊就剛剛好是list中第i個位置
# 就是level i的所有點，這就是為什麼要檢查len(Q) == level，如果成立代表現在在新的
# level，就新增一個新的list


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def Level_Order(root, level):
    if not root:
        return
    Same_Level = []
    # 現在在新的level，新增一個新的list
    if len(Q) == level:
        Q.append(Same_Level)

    Q[level].append(root.val)

    if root.left:
        Level_Order(root.left, level+1)
    if root.right:
        Level_Order(root.right, level+1)


# 生測資
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

Q = []
Level_Order(root, 0)
print Q
