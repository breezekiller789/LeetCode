#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/binary-tree-cameras/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.haha = 0

    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.haha = 0

        # state = 0, current node's children is not camera, so this node has
        # gotta be a camera
        # state = 1, current node's children is a camera, so this node is
        # covered
        # state = 2, current node's children is covered by children's children
        def DFS(root):
            global camera
            # 如果該節點是leaf，直接回傳0，因為他沒有兒子可以cover他，他也不可以
            # 是camera，因為把camera放在leaf很不值得，放leaf只能cover leaf跟他的
            # parent，如果放不是leaf的，他可以cover他的父親兒子還有兒子的兄弟，
            # 利益比較多。
            if not root.left and not root.right:
                return 0

            needCamera = False
            iAmCovered = False
            # 如果有左兒子，去拜訪他，並告訴我他的狀態是多少
            if root.left:
                state = DFS(root.left)
                # 如果兒子給我零，代表我就必須要是camera了
                if state == 0:
                    needCamera = True
                    iAmCovered = True
                # 如果是一，代表我兒子是camera，那我就可以不用是camera，我只是被
                # cover
                elif state == 1:
                    iAmCovered = True

            # 如果有右兒子，跟剛剛左兒子比照辦理。
            if root.right:
                state = DFS(root.right)
                if state == 0:
                    needCamera = True
                    iAmCovered = True
                elif state == 1:
                    iAmCovered = True
            # 如果我這個節點是攝影機，那我就回傳1讓我父母知道我是攝影機
            if needCamera:
                camera += 1
                return 1
            # 如果我不是攝影機，而且我被我兒子cover，回傳2
            if iAmCovered:
                return 2
            # 上面兩種情況都不是就回傳0
            return 0

        global camera
        camera = 0
        state = DFS(root)

        # 這一行的意思是說，如果回傳的state是零的話，代表現在root必須要是攝影機，
        # 就給他加一
        return camera if state != 0 else camera+1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
camera = 0
obj = Solution()
print obj.minCameraCover(root)
