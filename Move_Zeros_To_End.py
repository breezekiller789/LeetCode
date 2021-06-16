#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# output: [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0]
arr = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]

left = 0
for i, num in enumerate(arr):
    if num != 0:
        arr[left], arr[i] = arr[i], arr[left]
        left += 1
print arr
