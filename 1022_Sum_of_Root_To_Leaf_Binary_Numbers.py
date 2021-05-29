#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Preorder(root, String, result):
    if not root:
        return
    if not root.left and not root.right:
        result.append(String+str(root.val))
    String += str(root.val)
    Preorder(root.left, String, result)
    Preorder(root.right, String, result)


def Evaluate(num):
    Sum = 0
    count = 1
    for i in range(len(num)-1, -1, -1):
        if i == "0":
            count *= 2
            continue
        Sum += int(num[i])*count
        count *= 2
    return Sum


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)
# root.right.right.right = TreeNode(1)
result = []
Preorder(root, "", result)
Sum = 0
for binary in result:
    Sum += Evaluate(binary)
print Sum
