#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# Solution:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems

# Ref Question 714

prices = [3, 3, 5, 0, 0, 3, 1, 4]   # 6
prices = [1, 2, 3, 4, 5]            # 4


Ti10, Ti20 = 0, 0
Ti11, Ti21 = float("-inf"), float("-inf")
for idx, priceToday in enumerate(prices):
    Ti20 = max(Ti20, Ti21+priceToday)
    Ti21 = max(Ti21, Ti10-priceToday)
    Ti10 = max(Ti10, Ti11+priceToday)
    Ti11 = max(Ti11, -priceToday)
print Ti20
