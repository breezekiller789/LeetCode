#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

# All questions about stocks' solution:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems

# 這一題真的難...

prices = [1, 3, 2, 8, 4, 9]     # 8
fee = 2
prices = [1, 3, 7, 5, 10, 3]    # 6
fee = 3

hold = float("-inf")
sold = 0
for idx, priceToday in enumerate(prices):
    hold = max(hold, sold-priceToday)
    sold = max(sold, hold+priceToday-fee)
print sold
