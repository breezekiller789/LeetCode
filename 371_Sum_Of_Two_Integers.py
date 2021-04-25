#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/sum-of-two-integers/

# 1. add a, b, we first use "AND" operator to spot the positions where we have
# to carry in, for example,
#       0011  (AND
#       0111
#   -----------
#       0011
# and we store this AND result to a variable called carry in.

# 2. We then use XOR operator to do the actual ADD action, but XOR will only ADD
# numbers, it won't keep carries for us, that's why we need that carry from step
# 1

# 3. In the end, we shift our carry 1 bit to the left, and that's because the
# carries need to be added to the left, let me give you an example,
#       0011
#       0111  (Shift 1 bit
#  -----------
#       0110
# as you can see, when we add a carry, we add it to the next digit, not current
# digit that we are adding, that's why it's called carry, because it needs to be
# added to the next digit, if you still can't understand it, let me give you an
# decimal example, let's say we add 14 and 9, we first do 4+9 = 13, which we
# leave 3 to the current position, and carry 1 to the next digit, that's basicly
# what i'm trying to say here:)

# =======Code==========
a = 1
b = 2
while b != 0:
    carry_in = a & b
    a ^= b
    b = carry_in << 1
print a
