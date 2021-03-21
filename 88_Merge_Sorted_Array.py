#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/merge-sorted-array/

# 解答中的three pointer，很聰明的方法，阿一開始也都想不到，以為就是要用merge
# sort的方法，結果不是，因為題目有要求說要in-place，全部都放在nums1裡面，不可以用
# 額外空間，所以就卡了，一開始的想法都是從list頭做，但是反過來想，從屁股開始來做
# 才是對的，大的就放nums1最後面，用第三個指標指著，最後面放到哪裡，這樣就可以了

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1


# ================Code Starts=====================
p1 = m - 1      # 指著nums1的尾巴，這裡的尾巴是m，因為最後面是待會要放東西的。
p2 = n - 1      # 指著nums2的尾巴。
p = m + n - 1   # 指著nums1真正的尾巴，就真的指著最後面。
while p1 >= 0 and p2 >= 0:
    # p1, p2指著的值互相比，大的放上去nums1最後面，然後結束之後要移動指標。
    if nums1[p1] > nums2[p2]:
        nums1[p] = nums1[p1]
        p1 -= 1
        p -= 1
    elif nums1[p1] < nums2[p2]:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
    else:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

# 走來這裡可能會有些人沒有走完，要繼續讓他走完。
while p1 >= 0:
    nums1[p] = nums1[p1]
    p1 -= 1
    p -= 1
while p2 >= 0:
    nums1[p] = nums2[p2]
    p2 -= 1
    p -= 1
print nums1
