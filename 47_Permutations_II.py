#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/permutations/

# 速度挺慢的，但是程式碼很優雅：）
# nums = [1, 2, 3]
# nums = [0, 1]
nums = [1, 1, 2]
Ans = []


def swap(i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


def Permutation(i, n):
    if i == n:
        print nums
        if nums not in Ans:
            Ans.append(nums[:])
    else:
        j = i
        while j <= n:
            swap(i, j)
            Permutation(i+1, n)
            swap(i, j)
            j += 1


Permutation(0, len(nums)-1)
print Ans
