#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/longest-harmonious-subsequence/

nums = [1, 3, 2, 2, 5, 2, 3, 7]
# nums = [1, 2, 3, 4]
# nums = [1, 1, 1, 1]

Diffs = [0 for _ in range(len(nums))]
