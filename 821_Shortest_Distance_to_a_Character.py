#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/shortest-distance-to-a-character/


class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        prev = None
        for i, char in enumerate(s):
            # Find the first c
            if char == c:
                target = i
                break
        result =[]  # Store the answer
        for cur, char in enumerate(s):
            if cur == target:
                result.append(0)
                # Match, find a furthur c
                for i, tmp in enumerate(s[cur+1:], start=cur+1):
                    if tmp == c:
                        # found it
                        target = i
                        break
                else:
                    # Cannot find furthur c
                    target = None
                prev = cur
                continue
            if prev is None:
                # Very beginning, don't have previous, directly calculate the distance to the target
                result.append(target-cur)
                continue
            elif target is None:
                # Doesn't have next c, directly caculate distance to the previous
                result.append(cur-prev)
                continue

            # we will savely have prev, target, and cur != target
            result.append(min(target-cur, cur-prev))
        return result
