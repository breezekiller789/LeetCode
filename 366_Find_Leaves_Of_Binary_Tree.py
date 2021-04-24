#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/find-leaves-of-binary-tree/

# 1. use preorder traversal to traverse, if root.left is null and root.right is
# null, then this root is leaf, so add it to Leaf list, also , we have to pass
# in Leaf list and parent, cuz we need to remove leaf, to do that we need
# parents to do so.


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Preorder(root, Leaf, parent, Child_Direction):
    if not root:
        return
    # Current node is leaf
    if not root.left and not root.right:
        # Current node is left child
        if Child_Direction == "Left":
            parent.left = None
        # Current node is right child
        elif Child_Direction == "Right":
            parent.right = None
        # Enter this if statement only if there is only 1 node left
        else:
            Leaf.append(root.val)
            root = None
            # we have to return right here cuz we have set root to None
            return Leaf, None
        Leaf.append(root.val)
    Preorder(root.left, Leaf, root, "Left")
    Preorder(root.right, Leaf, root, "Right")
    return Leaf, root


def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print root.val
    Inorder(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

Leaf = []
while root:
    leaf, root = Preorder(root, [], root, None)
    Leaf.append(leaf)
print Leaf
