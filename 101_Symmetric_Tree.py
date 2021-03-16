#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/symmetric-tree/

# 如果是對稱的，代表我把他左右子樹其中一個人swap之後，兩個子樹會長一樣，因為對稱
# ，所以很簡單，我就先swap左子樹，然後比看看左右子樹一不一樣，這樣就好了。


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_Same_Tree(p, q):
    # Base Condition，當兩個樹都是空的，回傳true
    if not p and not q:
        return True
    elif p and q:
        # 該節點都一樣，要繼續比
        if p.val == q.val:
            # 若左子樹一樣，就比右子樹，直接用return的，很漂亮
            if is_Same_Tree(p.left, q.left):
                return is_Same_Tree(p.right, q.right)
        # 節點值不一樣直接回傳False
        else:
            return False
    # 會走到這裡代表p, q就直接不一樣了
    return False


def swap(root):
    if not root:
        return
    else:
        swap(root.left)
        swap(root.right)
        tmp = root.left
        root.left = root.right
        root.right = tmp


# 測資
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
swap(root.left)
print is_Same_Tree(root.left, root.right)
