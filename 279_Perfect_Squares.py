#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# https://leetcode.com/problems/perfect-squares/

n = 12

squareNumbers = [i**2 for i in range(math.sqrt(n)+1)]
print squareNumbers
