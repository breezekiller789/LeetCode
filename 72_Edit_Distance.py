#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/edit-distance/

# 很不直覺的dp，因為很難去寫出遞迴公式


word1 = "horse"
word2 = "ros"
# word1 = "intention"
# word2 = "execution"

length1 = len(word1)
length2 = len(word2)
dp = [[0 for _ in range(length2+1)] for _ in range(length1+1)]

for j in range(length2+1):
    dp[0][j] = j

for i in range(length1+1):
    dp[i][0] = i

for i in range(1, length1+1):
    for j in range(1, length2+1):
        up = dp[i-1][j]+1
        left = dp[i][j-1]+1
        upleft = dp[i-1][j-1]
        # 如果兩邊的上一個字元都不一樣，就要多一步，一樣的話就不用多做一步。
        if word1[i-1] != word2[j-1]:
            upleft += 1
        dp[i][j] = min(up, left, upleft)
print dp[-1][-1]
