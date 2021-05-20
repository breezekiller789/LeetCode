#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/word-search-ii/

# 題目顯然就是要用DFS解，我也用DFS解，就是遞迴。

# Output: ["eat", "oath"]
board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"]
]
words = ["oath", "pea", "eat", "rain"]

# Output: []
# board = [
#     ["a", "b"],
#     ["c", "d"]
# ]
# words = ["abcb"]

# Output: []
board = [["a", "a"]]
words = ["aaa"]

# Output: ["abbbababaa"]
board = [
    ["b", "b", "a", "a", "b", "a"],
    ["b", "b", "a", "b", "a", "a"],
    ["b", "b", "b", "b", "b", "b"],
    ["a", "a", "a", "b", "a", "a"],
    ["a", "b", "a", "a", "b", "b"]
]
words = ["abbbababaa"]


# 只要鄰居有match到，就去拜訪他
def RecursiveSearch(board, currentNode, string, Visited, m, n):
    if not string:
        return True
    x, y = currentNode
    Visited.add((x, y))
    if x >= 1 and board[x-1][y] == string[0] and (x-1, y) not in Visited:
        Visited.add((x-1, y))
        if RecursiveSearch(board, (x-1, y), string[1:], Visited, m, n):
            return True
    if y < n-1 and board[x][y+1] == string[0] and (x, y+1) not in Visited:
        Visited.add((x, y+1))
        if RecursiveSearch(board, (x, y+1), string[1:], Visited, m, n):
            return True
    if x < m-1 and board[x+1][y] == string[0] and (x+1, y) not in Visited:
        Visited.add((x+1, y))
        if RecursiveSearch(board, (x+1, y), string[1:], Visited, m, n):
            return True
    if y >= 1 and board[x][y-1] == string[0] and (x, y-1) not in Visited:
        Visited.add((x, y-1))
        if RecursiveSearch(board, (x, y-1), string[1:], Visited, m, n):
            return True
    return False


def WordSearch(board, string, result, m, n):
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            # 一比對到，就進去做DFS
            if char == string[0]:
                Visited = set((i, j))
                # RecursiveSearch會回傳true，如果有match到字串。
                if RecursiveSearch(board, (i, j), string[1:], Visited, m, n):
                    if string not in result:
                        result.append(string)


m = len(board)
n = len(board[0])
result = []
for string in words:
    WordSearch(board, string, result, m, n)
print result
