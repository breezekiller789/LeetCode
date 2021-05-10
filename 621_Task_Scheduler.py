#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/task-scheduler/

# Solution: https://www.youtube.com/watch?v=eGf-26OTI-A

"""
The idea is, we first count all the character's occurance and sort it. We did
all this because we approach the answer differently, we make all tasks idle, and
insert task in it, we first insert the most frequent task, and then go all the
way down to the least frequent, that's the reason we sort the array in the first
place, because we need to fill the idle slots from the most frequent to lowest
frequency, as all this is said and done, if there is idle slots left, then we
return idle slots + length of tasks, else, return length of tasks
"""

tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
# tasks = ["A", "A", "A", "B", "B", "B"]
# n = 0
# tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
# n = 2

charCount = [0 for _ in range(26)]

# Count out all characters
for char in tasks:
    charCount[ord(char)-ord('A')] += 1

charCount.sort()                    # Sort in ascending order
maxFrequency = charCount[-1]-1  # Minus 1 because we don't need to count the end
idleSlots = n * maxFrequency    # Count the idle slots

for idx in xrange(24, -1, -1):
    idleSlots -= min(maxFrequency, charCount[idx])
if idleSlots > 0:
    print len(tasks)+idleSlots
else:
    print len(tasks)
