#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/minimum-depth-of-binary-tree/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def MinDepth(root):
    if not root:
        return 0
    leftHeight = MinDepth(root.left)
    rightHeight = MinDepth(root.right)
    # 這一句比較特別，如果左右子樹最低是0，這樣不算，因為會是零不可能會是leaf
    return 1 + (min(leftHeight, rightHeight) or max(leftHeight, rightHeight))


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print MinDepth(root)
