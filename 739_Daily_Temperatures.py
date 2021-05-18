#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/daily-temperatures/

# 這一題要用stack做，並不直覺。準備一個stack，裡面都是放一堆index，我們從頭掃到
# 尾一次，然後每一次我們就去跟stack top的index所對應的溫度比較，如果我們現在的溫
# 度比stack top的溫度高，就pop堆疊頂端，然後更新那個index的距離，距離就簡單的把
# 現在位置扣掉剛剛堆疊頂端pop出來的位置就可以了，這樣一直pop，直到遇到stack空掉
# 或者遇到堆疊頂端的溫度比現在高。


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Stack = []
nextWarmerDay = [0] * len(temperatures)
for currentIndex, currentTemperature in enumerate(temperatures):
    # If stack top has lower temperature than current temperature then we have
    # to pop stack and update it's distance from now
    while Stack and temperatures[Stack[-1]] < currentTemperature:
        lastIndexToBeUpdated = Stack.pop()  # Pop stack top

        # Update stack top index's distance from now
        nextWarmerDay[lastIndexToBeUpdated] = currentIndex-lastIndexToBeUpdated
    # Push current index into stack
    Stack.append(currentIndex)
print nextWarmerDay
