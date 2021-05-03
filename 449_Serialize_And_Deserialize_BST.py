#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/serialize-and-deserialize-bst/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Codec(object):
    def __init__(self):
        self.String = ""

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        Q = [root]
        while Q:
            currentNode = Q[0]
            del Q[0]
            if currentNode == "null":
                self.String += "null,"
                continue
            else:
                self.String += "{},".format(currentNode.val)
            if currentNode.left:
                Q.append(currentNode.left)
            else:
                Q.append("null")
            if currentNode.right:
                Q.append(currentNode.right)
            else:
                Q.append("null")
        return self.String

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        self.String = []
        data = data.split(",")
        root = TreeNode(data[0])
        del data[0]
        Q = [root]
        while Q:
            currentRoot = Q[0]
            del Q[0]
            left = data[0]
            right = data[1]
            del data[0:2]
            if left != "null":
                leftNode = TreeNode(left)
                currentRoot.left = leftNode
                Q.append(leftNode)
            if right != "null":
                rightNode = TreeNode(right)
                currentRoot.right = rightNode
                Q.append(rightNode)
        return root


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
obj = Codec()
Preorder(obj.deserialize(obj.serialize(root)))
