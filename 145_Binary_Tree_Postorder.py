#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/binary-tree-postorder-traversal/


def Postorder(root):
    if not root:
        return
    Postorder(root.left)
    Postorder(root.right)
    print root.val
