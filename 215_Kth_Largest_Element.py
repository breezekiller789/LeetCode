#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/kth-largest-element-in-an-array/

# 資結Sorting章節，在講selection problem的時候講的，借用quick sort的partition
# function，然後再看有沒有命中k-th


def swap(i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


# 用的是演算法中的partition
def Partition(p, r):
    pivot = nums[r]
    i = p-1
    j = p
    # j領頭，i跟在j屁股後面
    while j < r:
        if nums[j] < pivot:
            i += 1
            swap(i, j)
            j += 1
            continue
        j += 1
    swap(i+1, r)
    return i+1


def Select(l_, u, k):
    if l_ <= u:
        # 先去找要insert在哪個位置，再和k去比，看是要往左找還是往右找。
        q = Partition(l_, u)
        print nums, l_, q, u, k
        # 命中，直接回傳。
        if q == k:
            return nums[k]
        # 會進這裡代表要往右，在q的右手邊。
        elif q < k:
            return Select(q+1, u, k)
        # 進這裡代表要往左，在q的左手邊。
        else:
            return Select(l_, q-1, k)


# nums = [3, 2, 1, 5, 6, 4]
# k = 2
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

print Select(0, len(nums)-1, len(nums)-k)
