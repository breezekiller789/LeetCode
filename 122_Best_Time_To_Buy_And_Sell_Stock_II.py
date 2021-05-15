#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Same solution of Question 714 but has 0 fee

prices = [1, 3, 2, 8, 4, 9]     # 8
prices = [1, 3, 7, 5, 10, 3]    # 6

hold = float("-inf")
sold = 0
for idx, priceToday in enumerate(prices):
    hold = max(hold, sold-priceToday)
    sold = max(sold, hold+priceToday)
print sold
