#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/2-keys-keyboard/

# I solved this using DP, and we go from 3 to n+1 because we want the index of
# the array matches n, that's why we need n+1, there are three cases, index is
# even, prime, odd. The idea is, if it is even number, we can use the
# dp[idx/2] and plus 2, why plus 2, because we only have to copy all and paste,
# 2 steps. For example, 8 = 4 * 2, aaaa -> copy all -> paste -> aaaaaaaa
# We can reuse previous condition, that's why we can use DP. If index is prime,
# directly put index into dp array. If odd, we find the greatest divisor use
# that condition to calculate current dp array.


def LargestDivisor(num):
    # Pick the greatest divisor
    for divisor in xrange(num/2, -1, -1):
        if num % divisor == 0:
            return divisor


def isPrime(num):
    # Check if this number is prime
    for idx in range(3, num//2):
        if num % idx == 0:
            return False
    return True


n = 3
n = 1
n = 9
n = 27

dp = [0 for _ in range(n+1)]
dp[0] = 0
dp[1] = 0
dp[2] = 2
for idx in range(3, n+1):
    # Even number, get the value of dp[idx/2] and plus 2
    if idx % 2 == 0:
        dp[idx] = dp[idx/2]+2
    # If it is prime, put index diretly in dp array
    elif isPrime(idx):
        dp[idx] = idx
    # If it not even and prime, this is definetly odd number, so we find the
    # greatest divisor, we divide it with largest divisor, that's means the
    # number of pastes we have to performe
    else:
        largeDivisor = LargestDivisor(idx)
        dp[idx] = idx/largeDivisor + dp[largeDivisor]
print dp[-1]
