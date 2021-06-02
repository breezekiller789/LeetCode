#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/paint-house/

# Recursion + memoization

# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house
# 2 into blue.
# Minimum cost: 2 + 5 + 3 = 10
costs = [
    [17, 2, 17],
    [16, 16, 5],
    [14, 3, 19]
]

# Output: 2
costs = [
    [7, 6, 2]
]

# Output: 26
costs = [
    [3, 5, 3],
    [6, 17, 6],
    [7, 13, 18],
    [9, 10, 18]
]

# Output: 55
costs = [
    [13, 8, 17],
    [6, 8, 19],
    [5, 1, 7],
    [5, 18, 2],
    [12, 3, 4],
    [12, 7, 10],
    [14, 16, 7],
    [19, 17, 19]
]


def RecursivePaint(costs, start, lastColorPicked, alreadyChecked):
    # Base case, 就是costs只剩下一間屋子，要小心不要直接回傳最小值，要避開上一個
    # 屋子的顏色，我是直接hard code
    if start == len(costs)-1:
        if lastColorPicked == 0:
            return min(costs[-1][1], costs[-1][2])
        elif lastColorPicked == 1:
            return min(costs[-1][0], costs[-1][2])
        elif lastColorPicked == 2:
            return min(costs[-1][0], costs[-1][1])
        # 會進來這裡就是input costs裡面就是只有一間房子
        else:
            return min(costs[-1])
    # 如果這間屋子我們剛剛已經有塗過油漆了，那就可以直接回傳這間屋子的最好油漆顏色
    # 一樣要避開上一個屋子的顏色！
    else:
        Min = float("inf")
        count = 0
        while count < 3:
            # 記得上一個屋子的顏色要避開
            if count != lastColorPicked and alreadyChecked[start][count]:
                Min = min(Min, alreadyChecked[start][count])
            count += 1
        if Min != float("inf"):
            return Min

    minCost = float("inf")
    for colorPicked in range(3):
        # 避開上一個屋子的顏色
        if colorPicked != lastColorPicked:
            ret = RecursivePaint(costs, start+1, colorPicked, alreadyChecked) +\
                costs[start][colorPicked]
            alreadyChecked[start][colorPicked] = ret
            minCost = min(minCost, ret)
        # 如果跟上一個屋子一樣顏色，沒關係，我們就不要進去一起算最小值，但是
        # alreadyChecked陣列還是要更新，這邊debug很久才找出來
        else:
            ret = RecursivePaint(costs, start+1, colorPicked, alreadyChecked) +\
                costs[start][colorPicked]
            alreadyChecked[start][colorPicked] = ret
    return minCost


alreadyChecked = [[None, None, None] for _ in range(len(costs))]
alreadyChecked[-1] = costs[-1]
print RecursivePaint(costs, 0, None, alreadyChecked)
