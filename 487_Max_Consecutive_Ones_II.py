#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/max-consecutive-ones-ii/

# Solution : https://leetcode.com/problems/max-consecutive-ones-ii/discuss/96946/Concise-Python-solution-good-for-follow-up-time-O(n)-space-O(1)

# It's really not easy to think.

nums = [1, 0, 1, 1, 0]
nums = [1, 1, 1, 0, 0, 0, 1, 0, 1, 1]
# nums = [1, 0, 1, 1, 0, 1]

# previousLength is initialize to -1 because in the beginning we haven't seen
# any 0 yet, if we get a test case like [1], we will return 2 if we set
# previousLength to 0
previousLength, currentLength, maxLength = -1, 0, 0
for num in nums:
    if num == 0:
        previousLength = currentLength
        currentLength = 0
    else:
        currentLength += 1
    maxLength = max(maxLength, previousLength+1+currentLength)
print maxLength
