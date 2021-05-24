#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

# Whenever the current element a is bigger than the previous element,
# we need at lease a - pre operations to make this difference.

# We accumulate the total number of the operations,
# this result is a lower bound and it's feasible.

# Output: 3
# Explanation: We need at least 3 operations to form the target array from the
# initial array.
# [0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
# [1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
# [1,2,2,2,1] increment 1 at index 2.
# [1,2,3,2,1] target array is formed.
target = [1, 2, 3, 2, 1]

# Output: 4
# Explanation: (initial)[0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] ->
# [3,1,1,2] (target).
target = [3, 1, 1, 2]

# Output: 7
# Explanation: (initial)[0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1]
# -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2] (target).
target = [3, 1, 5, 4, 2]

# Output: 1
# target = [1, 1, 1, 1]

res = pre = 0
for a in target:
    res += max(a - pre, 0)
    pre = a
print res
