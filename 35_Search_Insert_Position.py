#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/search-insert-position/

# nums = [1, 3, 5, 6]
# target = 5
# nums = [1, 3, 5, 6]
# target = 0
nums = [0]
target = 0
length = len(nums)
low = 0
high = length-1
mid = 0
while abs(low-high) > 1:
    mid = (low+high)/2
    if nums[mid] == target:
        print "Found at {}".format(mid)
        exit()
    elif nums[mid] > target:
        high = mid
    elif nums[mid] < target:
        low = mid

# 這邊還有希望會找到，但只有兩種情況，target落在low/high的位置上這兩種
if target == nums[low]:
    print "Found at {}".format(low)
    exit()
elif target == nums[high]:
    print "Found at {}".format(high)
    exit()

# 走到這裡代表target不存在nums裡，就找他應該在的位置
# target超過最大值，就放最大值下一個
if target > nums[high]:
    print high+1
# target超過最小值，就放最小值前一個，這邊要小心，如果low剛剛好落在index 0，小
# 心不要越界，所以要多一個if來檢查，如果小於零就印零就好
elif target < nums[low]:
    if low-1 <= 0:
        print 0
    else:
        print low-1
# 應付下面這種測資，當初沒有想到
# nums = [1, 3]
# target = 2
elif target > nums[low] and target < nums[high]:
    print low+1
else:
    print mid
print "Not Found"
