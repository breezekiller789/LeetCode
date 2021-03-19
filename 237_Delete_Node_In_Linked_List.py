#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/delete-node-in-a-linked-list/

# 這一題真的出的不是這麼理想，有點像腦筋急轉彎的題目XD，刪除節點，竟然只是搬動
# 資料而已，通常要刪除解點必須要知道上一個節點才能刪除，這個只給你要刪除的節點而
# 以，但是其實我覺得滿屌的一個題目啦，雖然留言區罵聲一片，但是還不錯。


class ListNode(object):
    def __init__(self, x=0):
        self.val = x
        self.next = None


node.val = node.next.val
node.next = node.next.next
