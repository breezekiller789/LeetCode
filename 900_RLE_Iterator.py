#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/rle-iterator/

# 這一題看似簡單，實作起來還真多細節，要做很多邊界檢查跟一些情況都要cover
# 這題基本上就是看邏輯跟細節


class RLEIterator(object):

    def __init__(self, encoding):
        """
        :type encoding: List[int]
        """
        self.encoding = encoding
        self.pointer = 0
        self.length = len(encoding)

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 如果指標沒有超出而且目前指標位置的數量都還夠提供，就回傳
        if self.pointer < self.length and self.encoding[self.pointer] - n >= 0:
            # 要記得扣掉庫存
            self.encoding[self.pointer] -= n
            return self.encoding[self.pointer+1]
        else:
            # 會來這裡就是目前指標的地方庫存不夠，必須要往後看有沒有其他庫存。
            while self.pointer < self.length and\
                    self.encoding[self.pointer] - n < 0:
                n -= self.encoding[self.pointer]  # 有庫存，用n去扣庫存，看夠不夠
                self.encoding[self.pointer] = 0  # 庫存扣成0
                self.pointer += 2   # 指標要往前走，走兩格因為下一個是商品

            # 如果指標已經走到底，然後n又大於零，代表全空。
            if self.pointer == self.length and n > 0:
                return -1
            else:
                # 還有庫存
                self.encoding[self.pointer] -= n
                return self.encoding[self.pointer+1]


# [8, 8, 8, 5, 5]
obj = RLEIterator([3, 8, 0, 9, 2, 5])
print obj.next(4)
print obj.next(1)
print obj.next(1)
print obj.next(2)
# obj = RLEIterator([784, 303, 477, 583, 909, 505])
