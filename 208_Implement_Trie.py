#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/implement-trie-prefix-tree/


class TrieNode(object):
    def __init__(self):
        self.isWord = False
        self.children = dict()


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
        currentNode.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
        return currentNode.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given
        prefix.
        :type prefix: str
        :rtype: bool
        """
        currentNode = self.root
        for char in prefix:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
        return True


obj = Trie()
obj.insert("apple")
obj.insert("banana")
# print obj.search("apple")
# print obj.search("applet")
# print obj.search("apple")
# print obj.startsWith("app")
# print obj.startsWith("apt")
