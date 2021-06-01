#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/unique-binary-search-trees-ii/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


n = 3


def Generate(start, end):
    if start > end:
        return [None]
    allTrees = []
    # 這個for loop在挑root
    for i in range(start, end+1):
        # 遞迴的去拿左邊的所有subtree
        leftSubTrees = Generate(start, i-1)
        # 遞迴的去拿右邊的所有subtree
        rightSubTrees = Generate(i+1, end)

        # 從左邊的subtree中從頭挑，然後跟右邊的所有subtree接再一起，然後這樣就
        # 是一隻新的tree，這樣所有排列組合都試過
        for leftsubtree in leftSubTrees:
            for rightsubtree in rightSubTrees:
                currentRoot = TreeNode(i)
                currentRoot.left = leftsubtree
                currentRoot.right = rightsubtree
                allTrees.append(currentRoot)
    return allTrees


print Generate(1, n)
