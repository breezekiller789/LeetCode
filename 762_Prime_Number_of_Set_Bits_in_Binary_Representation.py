#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

# 我覺得已經寫很漂亮了，但是還是TLE，討論區有一個一行程式碼的，長下面這樣，直接
# beat 91%，但是我完全看不懂在寫啥。
# return sum(665772 >> bin(i).count('1') & 1 for i in range(L, R+1))

left = 6
right = 10
left = 10
right = 15

numberOfOnes = [0] * (right+1)
isPrime = [True for _ in range(right+1)]
isPrime[0] = False
isPrime[1] = False
numberOfOnes[1] = 1
for num in range(right+1):
    numberOfOnes[num] = numberOfOnes[num >> 1] + (num & 1)

for i in range(2, right+1):
    if isPrime[i]:
        j = i
        while j * i <= right:
            isPrime[j*i] = False
            j += 1

Count = 0
for num in numberOfOnes[left:]:
    if isPrime[num]:
        Count += 1
print Count
