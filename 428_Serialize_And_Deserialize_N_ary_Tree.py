#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


root = Node(1, [])
root.children.extend([Node(3, []), Node(2, []), Node(4, [])])
root.children[0].children.extend([Node(5, []), Node(6, [])])
#                1
#         3      2       4
#      5     6


class Codec(object):
    # Level order traversal
    def serialize(self, root):
        Q = [root]
        while Q:
            currentNode = Q[0]
            print currentNode.val
            Q = Q[1:]
            for child in currentNode.children:
                Q.append(child)

    def deserialize(self, data):
        pass


obj = Codec()
obj.serialize(root)
