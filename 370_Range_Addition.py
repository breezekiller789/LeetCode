#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/range-addition/

# this method is actually very clever, we don't have to add on every node, we
# only have to add start node, and skip to the next node of end node, in the
# end, we sum up all the values from the beginning til the end, and that will
# bring back the values that we skipped in the first place. Let's explain this
# with the first example down below.
# [0, 0, 0, 0, 0]
# -> (1, 3, 2)
# -> [0, 2, 0, 0, -2], add 2 to node 1,skip the nodes between node 1 and node3+1
# -> (2, 4, 3)
# -> [0, 2, 3, 0, -2], add 3 to node 2,skip nodes between node 2 and node 4+1
# -> (0, 2, -2)
# -> [-2, 2, 3, 2, -2]

# Sum it up and put Sum in the position
# -> Sum = 0, Initial
# -> [-2, 2, 3, 2, -2], Sum = -2, current index = 0
# -> [-2, 0, 3, 2, -2], Sum = 0, current index = 1
# -> [-2, 0, 3, 2, -2], Sum = 3, current index = 2
# -> [-2, 0, 3, 5, -2], Sum = 5, current index = 3
# -> [-2, 0, 3, 5, 3], Sum = 3, current index = 4

length = 5
updates = [
    [1, 3, 2],
    [2, 4, 3],
    [0, 2, -2]
]
length = 10
updates = [
    [2, 4, 6],
    [5, 6, 8],
    [1, 9, -4]
]

result = [0 for _ in range(length)]

for element in updates:
    start, end, shift = element
    result[start] += shift
    if end < length-1:
        result[end+1] -= shift
print result
Sum = 0
for idx in range(0, length):
    Sum += result[idx]
    result[idx] = Sum
print result

# My first thought, got TLE:((
# result = [0 for _ in range(length)]

# for element in updates:
#     start, end, offset = element
#     idx = start
#     while idx <= end:
#         result[idx] += offset
#         idx += 1
# print result
