#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# 1. serialize, use level order traversal method to get all the nodes in the
# exact order, put the nodes in array, and transfer this array to a string, it
# will get passed to our deserialize function.

# 2. deserialize, use the string that we just made, and split it with coma, cuz
# we seperate them with coma, extract the data[0], it will be our root, and
# check if root is null, if yes, return directly, in the end, just extract two
# values from data, and malloc TreeNode to that value and assign, very similar
# to level order traversal but instead of getting node, we put new nodes in it


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Codec(object):

    def __init__(self):
        self.array = []

    # Level Order Traversal
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        Q = []
        Q.append(root)
        while Q:
            node = Q[0]
            self.array.append(node)
            Q = Q[1:]
            if not node:
                continue
            Q.append(node.left)
            Q.append(node.right)
        string = ""
        # Transfer the array to a string
        for node in self.array:
            if node:
                string += "{},".format(node.val)
            else:
                string += "null,"
        return string[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # added this cuz pylint keeps telling me to make this a function
        self.array = []

        data = data.split(",")
        if data[0] == "null":
            return
        root = TreeNode(int(data[0]))   # Extract Root
        data = data[1:]
        Q = [root]
        while Q and data:
            node = Q[0]
            left_node = data[0]
            right_node = data[1]
            Q = Q[1:]
            data = data[2:]
            if left_node != "null":
                newNode = TreeNode(int(left_node))
                node.left = newNode
                Q.append(newNode)
            if right_node != "null":
                newNode = TreeNode(int(right_node))
                node.right = newNode
                Q.append(newNode)
        return root


def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print root.val
    Inorder(root.right)


def Preorder(root):
    if not root:
        return
    print root.val
    Preorder(root.left)
    Preorder(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
Code = Codec()
data = Code.serialize(None)
Preorder(Code.deserialize(data))
