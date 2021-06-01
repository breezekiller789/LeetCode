#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections

# https://leetcode.com/problems/reveal-cards-in-increasing-order/

# 沒想到可以用deque來做，比較不直覺一點，原本想說先排序，然後分一半，這樣遞迴，
# 然後把遞迴傳回來的陣列一個個插進去左半邊。

# Output: [2,13,3,11,5,17,7]
# Explanation:
# We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter),
# and reorder it.
# After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top
# of the deck.
# We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
# We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
# We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
# We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
# We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
# We reveal 13, and move 17 to the bottom.  The deck is now [17].
# We reveal 17.
# Since all the cards revealed are in increasing order, the answer is correct.
deck = [17, 13, 11, 2, 3, 5, 7]
# [2, 3, 5, 7, 11, 13, 17]

Ans = [0] * len(deck)
index = collections.deque(range(len(deck)))

for card in sorted(deck):
    Ans[index.popleft()] = card
    if index:
        index.append(index.popleft())
print Ans
