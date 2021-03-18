#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/implement-trie-prefix-tree/

# 練習class, method, constructor...


class Trie(object):
    def __init__(self):
        self.Inserted = []

    def insert(self, word):
        self.Inserted.append(word)
        # print "Insert {}".format(word)
        # print self.Inserted

    def search(self, word):
        for i in self.Inserted:
            if i == word:
                return True
        return False

    def startsWith(self, prefix):
        length = len(prefix)
        for i in self.Inserted:
            if i[:length] == prefix:
                return True
        return False


trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("cat")
print trie.search("cat")
print trie.startsWith("appe")
