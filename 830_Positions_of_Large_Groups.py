#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/positions-of-large-groups/

# Output: [[3,6]]
# Explanation: "xxxx" is the only large group with start index 3 and end index 6
s = "abbxxxxzzy"

# Output: []
# Explanation: We have groups "a", "b", and "c", none of which are large groups
s = "abc"

# Output: [[3,5],[6,9],[12,14]]
# Explanation: The large groups are "ddd", "eeee", and "bbb"
s = "abcdddeeeeaabbbcd"

# Output: []
s = "aba"

result = []
interval = [0, 0]
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        interval[1] += 1
    else:
        if interval[1] - interval[0] + 1 >= 3:
            result.append(interval)
        interval = [i+1, i+1]
if interval[1] - interval[0] + 1 >= 3:
    result.append(interval)
print result
