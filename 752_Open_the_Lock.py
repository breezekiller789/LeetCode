#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/open-the-lock/

# 用BFS來解，完全沒想到可以用BFS，想法就是，從0000開始，我就把每一個數字都轉一下
# 加一或減一，然後把這些字串都放進queue裡面，一個一個去做，最後的結果就是BFS的
# level，就回傳level就好。

deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
deadends = ["8888"]
target = "0009"
deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
target = "8888"
deadends = ["0000"]
target = "8888"

# 先hash所有deadend
deadEndHash = set()
for string in deadends:
    deadEndHash.add(string)

Visited = set()
Q = ["0000"]
Level = 0
while Q:
    childCount = len(Q)
    count = 0
    while count < childCount:
        currentString = Q.pop(0)
        if currentString == target:
            print Level
            exit()
        if currentString in deadEndHash:
            print -1
            exit()
        for i in range(4):
            currentDigit = int(currentString[i])
            # 如果是遇到0 或者 9都要分開做，因為我們可以往迴轉，0減一會變9
            # 9加一會變0
            if currentDigit == 0:
                incremented = currentString[0:i]+"1"+currentString[i+1:]
                decremented = currentString[0:i]+"9"+currentString[i+1:]
            elif currentDigit == 9:
                incremented = currentString[0:i]+"0"+currentString[i+1:]
                decremented = currentString[0:i]+"8"+currentString[i+1:]
            else:
                incremented = currentString[0:i]\
                    + str(currentDigit+1) + currentString[i+1:]
                decremented = currentString[0:i]\
                    + str(currentDigit-1) + currentString[i+1:]

            # 把這些加一減一的字串放盡queue，但是要檢查又沒有看過跟屬於deadend
            if incremented not in deadEndHash and incremented not in Visited:
                Visited.add(incremented)
                Q.append(incremented)
            if decremented not in deadEndHash and decremented not in Visited:
                Visited.add(decremented)
                Q.append(decremented)
        count += 1
    Level += 1
print -1
