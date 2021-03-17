#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/longest-consecutive-sequence/

# 這一題看起來超簡單，做起來還真不簡單，因為要設一些flag，我是不知道有沒有更聰明
# 的方法，但是我的程式跑起來91.68%快，所以應該還行，我是先排序，然後下去算連續長
# 度，很直覺，重點就是在要怎麼算出最長連續長度，我就線性掃一次排序過的list，然後
# 設下層層的if-else去檢查，這些if-else不能夠換順序，詳細註解在程式碼中。

# 測資
# nums = [0, 2, 4, 3, 100, 101, 102, 50, 51, 52, 53]
nums = [1, 2, 0, 1]
# nums = [100, 4, 200, 201, 203, 204, 205, 206, 207, 1, 3, 2, 6]
# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

Sorted = sorted(nums)       # 先排序
Max = 1                     # 紀錄最長長度
Count = 1                   # 當有連續出現，記在這個變數裡
Status = ""                 # 紀錄現在連續的是遞增還是遞減
for idx, num in enumerate(Sorted[1:], start=1):
    # 有重複直接跳下一個，不用多檢查
    if num == Sorted[idx-1]:
        continue
    # 現在的值是上一個值加一，而且現在狀態是遞增，就進去加一
    if num == Sorted[idx-1]+1 and Status == "Ascending":
        Count += 1
    # 現在是上一個減一，且狀態是遞減，就進去加一
    elif num == Sorted[idx-1]-1 and Status == "Descending":
        Count += 1
    # 現在是上一個加一，但是狀態卻是遞減，代表要停下來，例如下面這種情況
    # 5, 4, 3, 2, 3
    elif num == Sorted[idx-1]+1 and Status == "Descending":
        # 結算Count
        if Count > Max:
            Max = Count
        Count = 1
        Status = ""
    # 現在是下一個減一，但是狀態卻是遞增，要停下來，例如下面這種情況
    # 1, 2, 3, 4, 3
    elif num == Sorted[idx-1]-1 and Status == "Ascending":
        # 結算Count
        if Count > Max:
            Max = Count
        Count = 1
        Status = ""

    # 會進來這裡通常都是最一開始準備要遞增才會進來這裡，所以才會放在很下面檢查
    # 因為開始遞增或遞減的情形相對起來會比較少，因為一旦遞增遞減，就會一直下去
    # 如果這個放最上面檢查就會比較浪費時間。
    elif num == Sorted[idx-1]+1:
        Count = 2
        Status = "Ascending"

    # 這個和上一個一樣道理，只是是遞減
    elif num == Sorted[idx-1]-1:
        Count = 2
        Status = "Descending"
    # 跨間隔，清算Count，例如下面這種。
    # 1, 2, 3, 100, 200, 300
    else:
        if Count > Max:
            Max = Count
        Count = 1
        Status = ""
if Count > Max:
    Max = Count
print Max
