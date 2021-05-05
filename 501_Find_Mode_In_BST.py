#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/find-mode-in-binary-search-tree/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Inorder(root, Seen, Max):
    if not root:
        return Max
    Max = Inorder(root.left, Seen, Max)
    if str(root.val) not in Seen:
        Seen[str(root.val)] = 1
    else:
        Seen[str(root.val)] += 1
    Max = max(Max, Seen[str(root.val)])
    Max = Inorder(root.right, Seen, Max)
    return Max


root = TreeNode(1)
root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(3)

if not root.left and not root.right:
    print [root.val]
Seen = dict()
Max = Inorder(root, Seen, 0)
Ans = []
for element in Seen:
    if Seen[element] == Max:
        Ans.append(int(element))
print Ans
