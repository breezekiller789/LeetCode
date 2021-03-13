#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/generate-parentheses/
# import pdb
# 現在這個是解答的方法，叫backtracking，有夠聰明，用遞迴的方式去解，主要就是滿足
# 兩個條件，一個是'('數一定要小於n，然後')'數一定要小於'('數，解答影片在下方，很
# 棒的解法，時間空間複雜度要想一下...
# Time : bounded by Catalan Number O(4^n / n^1/2)
# Space : O(n)
# https://www.youtube.com/watch?v=s9fokUqJ76A&ab_channel=NeetCode


def backtrack(s='', left=0, right=0):
    if len(s) == 2*n:
        Answer.append(s)
        return
    if left < n:
        backtrack(s+'(', left+1, right)
    if right < left:
        backtrack(s+')', left, right+1)


n = 6
Answer = []
backtrack()
print Answer

# def swap(i, j):
#     tmp = List[i]
#     List[i] = List[j]
#     List[j] = tmp


# def perm(i, n):
#     if i == n:
#         Permutations.append(List[:])
#         # print List
#     else:
#         j = i
#         while j <= n:
#             swap(i, j)
#             perm(i+1, n)
#             swap(i, j)
#             j += 1


# Permutations = []
# Answer = []
# n = 6
# stack = []
# List = ["(" for x in range(n)]
# List.extend([")" for x in range(n)])
# perm(0, 2*n-1)
# del List[:]
# # print Permutations
# for i in Permutations:
#     for char in i:
#         if char == '(':
#             stack.append(char)
#             continue

#         if not stack:
#             # print i, "false"
#             break
#         else:
#             if stack[-1] == ')':
#                 # print i, "false"
#                 break
#             else:
#                 stack.pop()
#     else:
#         # print i, "true"
#         if i not in Answer:
#             Answer.append(i)
#     del stack[:]
# Answer = ["".join(x) for x in Answer]
# print Answer
