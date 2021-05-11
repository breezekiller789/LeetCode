#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/replace-words/


dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
# dictionary = ["a", "b", "c"]
# sentence = "aadsfasf absbs bbab cadsfafs"
# dictionary = ["a", "aa", "aaa", "aaaa"]
# sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
# dictionary = ["catt", "cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
dictionary = ["ac", "ab"]
sentence = "it is abnormal that this solution is accepted"
dictionary = ["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"

hashTable = dict()
for string in dictionary:
    if string not in hashTable:
        hashTable[string] = 0
sentences = sentence.split(" ")
for i, string in enumerate(sentences):
    length = len(string)
    for idx in range(length):
        if string[0:idx+1] in hashTable:
            sentences[i] = string[0:idx+1]
            break
print " ".join(sentences)
