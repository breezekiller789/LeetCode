#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/word-search/

# 用DFS來解

# Output: true
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]
word = "ABCCED"

# Output: true
# board = [
#     ["A", "B", "C", "E"],
#     ["S", "F", "C", "S"],
#     ["A", "D", "E", "E"]
# ]
# word = "SEE"

# Output: false
# board = [
#     ["A", "B", "C", "E"],
#     ["S", "F", "C", "S"],
#     ["A", "D", "E", "E"]
# ]
# word = "ABCB"

board = [
    ["A", "B", "C", "E"],
    ["S", "F", "E", "S"],
    ["A", "D", "E", "E"]
]
word = "ABCEFSADEESE"


def RecursiveSearch(board, word, startNode, startIndex, m, n, Seen):
    if startIndex == len(word):
        return True
    x, y = startNode
    Seen.add(startNode)
    # Up
    if x >= 1 and board[x-1][y] == word[startIndex] and (x-1, y) not in Seen:
        if RecursiveSearch(board, word, (x-1, y), startIndex+1, m, n, Seen):
            return True

    # Right
    if y < n-1 and board[x][y+1] == word[startIndex] and (x, y+1) not in Seen:
        if RecursiveSearch(board, word, (x, y+1), startIndex+1, m, n, Seen):
            return True

    # Down
    if x < m-1 and board[x+1][y] == word[startIndex] and (x+1, y) not in Seen:
        if RecursiveSearch(board, word, (x+1, y), startIndex+1, m, n, Seen):
            return True

    # Left
    if y >= 1 and board[x][y-1] == word[startIndex] and (x, y-1) not in Seen:
        if RecursiveSearch(board, word, (x, y-1), startIndex+1, m, n, Seen):
            return True

    # 加這句，代表說這是一條死路，把我自己從Seen拿掉，因為可能走別條路可以
    Seen.remove(startNode)
    return False


m = len(board)
n = len(board[0])
for i, row in enumerate(board):
    for j, char in enumerate(row):
        Seen = set()
        if char == word[0] and RecursiveSearch(board, word, (i, j), 1, m, n,
                                               Seen):
            print True
            exit()
print False
