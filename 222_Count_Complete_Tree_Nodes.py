#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/count-complete-tree-nodes/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Count(root):
    if not root:
        return 0
    else:
        L_Count = Count(root.left)
        R_Count = Count(root.right)
        return L_Count + R_Count + 1
