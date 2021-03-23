#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/count-primes/

# Sieve of Eratosthenes的核心概念是用消去的方法，一開始我們就準備size為n的陣列
# 陣列都是布林值，我們從頭把那些不可能是質數的位置改成false，最後再算出陣列中是
# true的個數就好，那他的想法是，一個數的平方不可能是質數，就像13^2 = 169，不可能是
# 質數，再者，一個數平方往後的倍數，一定也不是質數，以下舉例，
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# 3 * 6 = 18
#     ...
#     ...
#     ...
# 所以我們從2開始往後面刪，把是倍數的都改成false，最後做完就會只剩下質數。

n = 100

# =========Code Starts============

# Sieve of Eratosthenes
if n < 2:
    print 0
is_Prime = [True for i in range(n)]     # 先都假設全部是質數。
is_Prime[0] = False         # 0不是質數，阿也不用去看，直接放False
is_Prime[1] = False         # 1也不是質數，直接False
for i in range(2, n):       # 從2開始一個一個往後，因為質數是從2開始。
    if is_Prime[i]:         # 如果flag是true，代表該數平方之後，以及比平方還要大
        j = i               # 的往後的倍數，一定也不是質數。
        while i * j < n:
            is_Prime[i * j] = False     # 往後的倍數一定不會是質數。
            j += 1
print is_Prime.count(True)


# # 我的暴力解法，很暴力。
# def Is_Prime(num):
#     flag = True
#     start = 2
#     while start <= num/2 and flag:
#         if num % start == 0:
#             flag = False
#             break
#         start += 1
#     return flag


# Primes = []

# Index = 2
# if n < 2:
#     print Primes
# if n == 2:
#     print [2]
# while Index < n:
#     if Is_Prime(Index):
#         Primes.append(Index)
#     Index += 1
# print Primes
