#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/valid-perfect-square/

# 1. starts with 1, 1*1, 2*2, 3*3..., if n*n > num then return False, if
# n*n==num then return True
# 2. Or we use Binary Search

# ==========Code===========
num = 104976

# Method 1
# n = 1
# while n*n < num:
#     n += 1
# if n*n == num:
#     print True
# else:
#     print False

# Method 2, Binary search

low = 1
high = num
while low < high:
    mid = (low+high)//2
    if mid**2 > num:
        high = mid
    elif mid**2 < num:
        low = mid+1
    else:
        print True
        exit()
print False
