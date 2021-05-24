#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/delete-nodes-and-return-forest/

# 用level order traversal，然後就要記錄節點的父母，當遇到要刪除的節點的時候就
# 去父母節點中把現在自己刪掉，然後把我的左右兒子加到result裡面，這樣我就不見了，
# 當中有一些小細節就是parent可能為空，兒子可能為空等等的要注意而已。


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def LevelOrderTraversal(root, to_delete):
    Q = [(root, None, None)]
    result = [root]
    while Q:
        currentNode, parent, Direction = Q.pop(0)
        # 左右兒子加到queue中
        if currentNode.left:
            Q.append((currentNode.left, currentNode, "left"))
        if currentNode.right:
            Q.append((currentNode.right, currentNode, "right"))

        # 現在這個點是要刪除的
        if currentNode.val in to_delete:
            # 我現在這個node要刪掉的，但是剛剛我放進去result裡，要拿掉
            if currentNode in result:
                result.remove(currentNode)

            # 我要被刪掉，所以要去把父母指向我的指標改掉。
            if parent and Direction == "left":
                parent.left = None
            elif parent and Direction == "right":
                parent.right = None

            # 最後就是把我的左右兒子打散放在result裡
            if currentNode.left:
                result.append(currentNode.left)
            if currentNode.right:
                result.append(currentNode.right)
    return result


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
to_delete = [1, 3]
result = LevelOrderTraversal(root, to_delete)
