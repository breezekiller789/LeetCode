#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/course-schedule/

# 用DFS來檢查有無cycle，首先這個graph必須是要是directed graph。
# 方法就是apply DFS然後檢查有沒有back edge，有back edge就是有cycle，資結跟演算法
# 都有教，教科書是用顏色來分辨是否為back edge，我這邊就用數字來表示，Visited
# list中，零代表還沒有拜訪過，一代表剛剛走過，二代表已經完成拜訪了，會有back
# edge就是說，我前方這個節點，是我們剛剛才走過的節點，這樣就是代表有cycle了。

numCourses = 2
prerequisites = [[1, 0], [0, 1]]

# ==========Code Starts===========


def DFS(graph, node, Visited):
    # Visited == 1代表我們剛剛走過這個點，而且還沒完成拜訪，代表有cycle
    if Visited[node] == 1:
        return False
    Visited[node] = 1
    for neighbor in graph[node]:
        # 如果這個節點還沒有完全拜訪，就去拜訪他，如果拜訪的結果是false，
        # 代表就是有cycle
        if Visited[neighbor] <= 1 and not DFS(graph, neighbor, Visited):
            return False
    Visited[node] = 2
    return True


Visited = [0 for _ in range(numCourses)]
graph = [[] for _ in range(numCourses)]
for course, prerequisite in prerequisites:
    graph[prerequisite].append(course)

for i in range(numCourses):
    # 還沒有拜訪過的點，就去拜訪他。
    if Visited[i] == 0 and not DFS(graph, i, Visited):
        print False
        exit()
print True
