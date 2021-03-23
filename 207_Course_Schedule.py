#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/course-schedule/

# 用DFS檢查有無cycle，因為topological
# sort的graph不可以有cycle，而有向圖中檢查cycle就是用DFS

numCourses = 2
prerequisites = [[1, 0], [0, 1]]

# ==========Code Starts===========
