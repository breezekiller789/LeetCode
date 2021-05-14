#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/top-k-frequent-words/

# Hashing and sorting. To be honest, after hashing, i was wanting to use max
# heap to store the datas and the only thing left is to extract root k times,
# and that's it, it will be so much faster but python doesn't have max heap
# library so i didn't do it that way, i chose using sorting.

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
# words = ["aaa", "aa", "a"]
# k = 1

# Hashing all words
hashTable = dict()
for word in words:
    if word not in hashTable:
        hashTable[word] = 1
    else:
        hashTable[word] += 1

Q = []      # Q is used for storing the datas in hash table
Ans = []    # Store answers
for element in hashTable:
    Q.append((-hashTable[element], element))

# Sort
Q.sort(reverse=1)
while k > 0:
    Ans.append(Q.pop()[1])
    k -= 1
print Ans
