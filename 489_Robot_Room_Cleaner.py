#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/robot-room-cleaner/

# 用DFS解，遞迴版本的DFS

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell
#        Returns false if the cell in front is blocked and robot stays in the
#        current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # 總共有四個方向，上下左右，(0, 1), (0, -1), (-1, 0), (1, 0)
        Visited = set()
        def DFS(robot, currentPosition, xDirection, yDirection, Visited):
            robot.clean()   # 直接清現在的位置
            x, y = currentPosition
            Visited.add(currentPosition)
            for _ in range(4):  # 四個方向都要拜訪。
                xNeighbor = x + xDirection  # 算出鄰居的位置。
                yNeighbor = y + yDirection  # 算出鄰居的位置
                # 如果這個鄰居位置我還沒拜訪過而且那個地方是可以去的，就去拜訪他
                if (xNeighbor, yNeighbor) not in Visited and robot.move():
                    DFS(robot, (xNeighbor, yNeighbor), xDirection, yDirection, Visited)

                    # 這邊一系列動作就是說，我拜訪完鄰居之後，我要把我的機器轉回
                    # 來原本的樣子，就是先轉180然後再移動一格回來，再轉180回去朝
                    # 向他原本的方向。
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()

                robot.turnLeft()    # 轉方向，去拜訪其他鄰居，要往右轉也是可以

                # 這一句很厲害，討論區看到的，這一句就直接包含了我們定義的四個方
                # 向，上下左右，最一開始方向是往上，也就是(0, 1)，這一句執行之後
                # 下一個方向會變成(-1, 0)，變成左邊，在下一次執行變成(0, -1)，就
                # 是往下，在下一次執行變(1, 0)變成右邊，很厲害！！單單這一句就涵
                # 括了四種情況，超棒。
                xDirection, yDirection = -yDirection, xDirection
        DFS(robot, (0, 0), 0 ,1, Visited)
