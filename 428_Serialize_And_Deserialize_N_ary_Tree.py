#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


root = Node(1, [])
root.children.extend([Node(3, []), Node(2, []), Node(4, [])])
root.children[1].children.extend([Node(5, []), Node(6, [])])
#                1
#         3      2       4
#      5     6


class Codec(object):
    # Level order traversal
    def serialize(self, root):
        Q = [root]
        Result = []
        String = ""
        while Q:
            nodesOfCurrentLevel = len(Q)
            Result.append([])
            while nodesOfCurrentLevel > 0:
                currentNode = Q[0]
                if currentNode == "null":
                    String += "null,"
                    Q = Q[1:]
                    nodesOfCurrentLevel -= 1
                    continue
                Q = Q[1:]
                String += "{},".format(currentNode.val)
                Result[-1].append(currentNode.val)
                for child in currentNode.children:
                    Q.append(child)
                if not currentNode.children:
                    Q.append("null")
                nodesOfCurrentLevel -= 1
            String += "null,"
        print String[:-1].split(",")
        return String[:-1].split(",")

    def deserialize(self, data):
        root = Node(data[0], [])
        data = data[2:]
        Q = [root]
        while Q:
            nodesOfCurrentLevel = len(Q)
            while nodesOfCurrentLevel > 0:
                currentNode = Q[0]
                Q = Q[1:]
                while data[0] != "null":
                    newNode = Node(data[0], [])
                    currentNode.children.append(newNode)
                    Q.append(newNode)
                    data = data[1:]
                data = data[1:]
                nodesOfCurrentLevel -= 1
        return root


obj = Codec()
newroot = obj.deserialize(obj.serialize(root))
obj.serialize(newroot)
