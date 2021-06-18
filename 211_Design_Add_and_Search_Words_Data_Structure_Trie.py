#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/design-add-and-search-words-data-structure/


class TrieNode(object):

    """Trie data structure"""

    def __init__(self):
        self.children = dict()
        self.isWord = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
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
        :type word: str
        :rtype: bool
        """
        currentNode = self.root
        for i in range(len(word)):
            if word[i] == ".":
                return self.RecursiveSearch(word[i+1:], currentNode.children)
            if word[i] not in currentNode.children:
                return False
            currentNode = currentNode.children[word[i]]
        return currentNode.isWord

    def RecursiveSearch(self, word, node):
        currentNode = node
        for i in range(len(word)):
            if word[i] == ".":
                return self.RecursiveSearch(word[i+1:], currentNode.children)
            if word[i] not in currentNode.children:
                return False
            currentNode = currentNode.children[word[i]]
        return currentNode.isWord
