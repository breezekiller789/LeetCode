#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/explore/interview/card/google/59/array-and-strings/3057/


# Output "eeebffff"
s = "abcd"
indexes = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]

# Output "eeecd"
# s = "abcd"
# indexes = [0, 2]
# sources = ["ab", "ec"]
# targets = ["eee", "ffff"]

# Output vbfrssozp
s = "vmokgggqzp"
indexes = [3, 5, 1]
sources = ["kg", "ggq", "mo"]
targets = ["s", "so", "bfr"]


infos = []      # 先把所有資訊都放進這裡，因為我們要做排序，依照index去排

for i, index in enumerate(indexes):
    infos.append([index, sources[i], targets[i]])

infos.sort()    # 排序
shiftAmount = 0
for i, info in enumerate(infos):
    # Get the actual position of replacement because we will change the length
    actualIndex = info[0] + shiftAmount

    # Skip if we cannot match the souce string
    if s[actualIndex:actualIndex+len(info[1])] != info[1]:
        continue

    stringBefore = s[0:actualIndex]     # String before replace string
    stringToBeReplaced = info[2]        # The actual replace string

    # Check for boundry because we might go over boundry
    if actualIndex+len(info[1]) >= len(s):
        stringAfter = ""
    else:
        stringAfter = s[actualIndex+len(info[1]):]

    s = stringBefore + stringToBeReplaced + stringAfter  # Merge all the strings

    # We have to get the shift amount because we might change the length
    shiftAmount += len(info[2]) - len(info[1])
print s
