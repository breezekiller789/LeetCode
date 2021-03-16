#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/same-tree/

# 資結第五章有教過，用遞迴去解


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


# 生測資
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print is_Same_Tree(p, q)
