#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/binary-tree-right-side-view/

# 這一題我一開始誤解題目，我以為我們人是站在root往右邊看，結果不是，題目是說想像
# 右手邊有一道平行光打向樹這邊，要我們列出所有被光打到的節點，像我一開始以為
# [1, 2]這個測資應該回傳[1]就行，結果是要回傳[1, 2]因為2右邊沒有節點，他也會被光
# 線打到
# 討論區有各種做法，但是其實很簡單，preorder traversal就可以完成了，只是我們要記
# 錄depth，然後一開始就記錄這一個depth的節點值，最左邊的節點會先被拜訪，但是當我
# 們拜訪右邊的節點的時候，左邊的就會被我們蓋掉，這正好是我們要的，我們就是用一個
# levelThatHitTheLight字典來記錄就好，記錄說每一個節點最右邊的是誰，最後回傳這個


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.haha = 0

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.haha = 0
        levelThatHitTheLight = dict()

        def Preorder(root, depth):
            if not root:
                return
            # 一開始就更新，只要後來有人也是同一層的，就會蓋掉左邊先拜訪的人
            levelThatHitTheLight[depth] = root.val
            Preorder(root.left, depth+1)
            Preorder(root.right, depth+1)

        Preorder(root, 0)
        return levelThatHitTheLight.values()


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

obj = Solution()
print obj.rightSideView(root)
