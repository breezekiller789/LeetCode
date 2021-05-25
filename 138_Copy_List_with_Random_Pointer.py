#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/copy-list-with-random-pointer/

# 我的想法說起來很複雜，但是觀念很簡單，就是hashing，一開始就是要建立一條新的linked
# list，這條新的是單純的singly linked list，還沒有給random pointer值，建立這條
# linked list的同時，我們要順便hash原始linked list的所有node，並給他們一個id，
# 為什麼要給id待會會講到，到這邊結束之後，我們就有一條新linked list，這時候我們也
# 是走一次這個新的linked list，然後hash所有node，這時候hash的key就不是用node去
# hash，是用剛剛我們給的id去當作key，value才放我們的node，原因是這樣，我們待會要
# 幫新的linked list接上random pointer的時候，要先去原始的node.random找，看他原本
# 指到誰，就先去指到的那個人拿他的id，然後我拿著這個id來query我新的node，看他對應
# 來新的linked list的node是誰，這樣我們才能指到對的節點，就這樣，其實就是一連串
# 的query。


# Definition for a Node.
class Node(object):
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def __init__(self):
        self.haha = 0

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        self.haha = 0
        if not head:
            return

        newHead = Node(head.val)
        origintmp = head.next
        originHash = {head: 0}
        tmp = newHead
        i = 1

        # 先做一條新的list，然後順便hash所有原始的node，i當作value，這裡的i就是id
        while origintmp:
            originHash[origintmp] = i   # hash, 用i當作id
            tmp.next = Node(origintmp.val)  # 做一個新的節點，指過去。
            tmp = tmp.next
            origintmp = origintmp.next
            i += 1  # id加一
        originHash[None] = i    # 這一步是因為我也要hash None，因為屁股是None

        # 現在就是要進去新的linked list裡面走一次，hash所有節點，但是是以id為key
        newHash = dict()
        tmp = newHead
        i = 0
        while tmp:
            newHash[i] = tmp    # 用id 當作key，節點為value
            tmp = tmp.next
            i += 1
        newHash[i] = None   # 這裡跟剛剛一樣，我也要hash None，因為屁股都是None

        # 到這裡就是只剩下一堆mapping工作。
        origintmp = head
        newtmp = newHead
        while origintmp:
            # 去原本的node看他random指到誰，拿著他去看他對應的id是多少。
            randomID = originHash[origintmp.random]

            # 再拿這個id去我們新的linked list hash table裡面看到底是哪個node
            actualNodeOfRandomPointer = newHash[randomID]

            # 新的節點的random pointer就可以接上了
            newtmp.random = actualNodeOfRandomPointer

            newtmp = newtmp.next
            origintmp = origintmp.next
        return newHead
