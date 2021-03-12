#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/valid-parentheses/

s = "(]"

Dict = {')': '(', ']': '[', '}': '{'}

stack = []
for i in list(s):
    # 遇到左括號就直接push()，無庸置疑。
    if i == '(' or i == '[' or i == '{':
        stack.append(i)
        continue
    # 遇到右括號的話，先檢查stack是不是空，空的就有問題，不是空的再繼續檢查括號
    if not stack:
        print "false"
        exit()
    else:
        # 來這邊就代表可以pop，但是要先檢查stack top是不是一個合法的括號，如果
        # 現在i是']'，但是stack top是'('而不是'['，這代表有問題，也要error
        if stack[-1] != Dict.get(i):
            print "false"
        else:
            stack.pop()
if stack:
    print "false"
else:
    print "true"
