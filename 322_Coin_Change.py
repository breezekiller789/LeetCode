#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/coin-change/

# 我用BFS來解，還不錯，給我這個想法的是Question 752，解鎖的一道題目，就是用BFS
# ，想法就是，我就都每一種可能性都做一步，慢慢往外擴展，就像是解鎖那道題依樣，我
# 把鎖每個環都轉一步，放進Queue裡頭，然後每一步就在往外擴展。

coins = [1, 2, 5]
amount = 11
# coins = [2]
# amount = 3
# coins = [1]
# amount = 0
# coins = [1]
# amount = 1
# coins = [1]
# amount = 2
Visited = set(str(amount))
Q = [amount]
Level = 0
while Q:
    childCount = len(Q)
    count = 0
    while count < childCount:
        currentAmount = Q.pop(0)
        if currentAmount == 0:
            print Level
            exit()
        elif currentAmount < 0:
            count += 1
            continue
        for coin in coins:
            if currentAmount-coin == 0:
                print Level+1
                exit()
            if str(currentAmount-coin) not in Visited:
                Q.append(currentAmount-coin)
                Visited.add(str(currentAmount-coin))
        count += 1
    Level += 1
print -1
