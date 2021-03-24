#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/flip-equivalent-binary-trees/

# =========Code Starts===========
#        1
#     2    3
#   4  5  6
#     7 8
#
#       1
#    3     2
#     6  5   4
#       8 7

def swap(root):
    if not root:
        return
    else:
        swap(root.left)
        swap(root.right)
        tmp = root.left
        root.left = root.right
        root.right = tmp


def Equivalent(root1, root2):
    if not root1 and not root2:
        return True
    elif root1 and root2:
        if root1.val == root2.val:
            if Equivalent(root1.left, root2.left):
                return Equivalent(root1.right, root2.right)
    else:
        return False
