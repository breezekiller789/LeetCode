#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/nim-game/

# 1. The though is, cuz we can start first, so if we left 4 to my friend, he is
# gonna lose no matter what, but if we want to make sure we left 4 to him, we
# have to make sure we left 8 to him, and now you get the point, if we left
# multiple of 4 to the other, we win, else we lose, unless the other doesn't
# know how this works.


# =========Code==========
n = 4
print n % 4 != 0
