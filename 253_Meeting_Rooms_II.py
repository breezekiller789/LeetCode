#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq

# https://leetcode.com/problems/meeting-rooms-ii/

# We don't quite care about start time, we care more about end time. We want to
# keep the earliest ending event as highest priority, so that's why we use
# min-heap to store the end time of event

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

intervals.sort()        # Sort first
heap = []
for interval in intervals:

    # If there is no overlap, no need to add room, but we still need to update
    # the earliest ending meeting.
    if heap and interval[0] >= heap[0]:
        heapq.heapreplace(heap, interval[1])

    # Enter this if there is a overlap push the current event's end time to the
    # heap
    else:
        heapq.heappush(heap, interval[1])
print len(heap)
