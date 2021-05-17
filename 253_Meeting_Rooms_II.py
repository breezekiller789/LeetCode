#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq

# https://leetcode.com/problems/meeting-rooms-ii/

intervals = [
    [0, 30],
    [5, 10],
    [15, 20]
]
# intervals = [
#     [7, 10],
#     [2, 4]
# ]
intervals = [
    [1, 3],
    [2, 6],
    [8, 10],
    [15, 18]
]

intervals.sort()
heap = []
for interval in intervals:
    print heap
    if heap and interval[0] >= heap[0]:
        heapq.heapreplace(heap, interval[1])
    else:
        heapq.heappush(heap, interval[1])
print heap
print len(heap)
