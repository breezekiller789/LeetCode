#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
# https://leetcode.com/problems/group-shifted-strings/

# Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

# Output: [["a"]]
# strings = ["a"]

diffs = collections.defaultdict(list)
for string in strings:
    currentDiffs = []
    for i in range(len(string)-1):
        currentDiffs.append((ord(string[i+1])-ord(string[i])) % 26)
    if tuple(currentDiffs) in diffs:
        diffs[tuple(currentDiffs)].append(string)
    else:
        diffs[tuple(currentDiffs)] = [string]
print [diffs[element] for element in diffs]
