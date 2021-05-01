#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/longest-palindrome/

# 1. Implement with hash tables, count out all the characters
# 2. Scan the whole hash table, if it is even, add it to Sum, and if it's odd,
# add that odd minus 1 to Sum

# ===========Code==========

s = "abccccdd"
s = "bananas"
# s = "zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez"
s = "a"
# s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"

Appearances = {}
for char in s:
    if char not in Appearances:
        Appearances[char] = 1
    else:
        Appearances[char] += 1
print Appearances
Count = 0
hasOne = False
Max = 0
for element in Appearances:
    # If it's even number, add it directly
    if Appearances[element] % 2 == 0:
        Count += Appearances[element]
    # It's odd, then add odd-1, for example, if this character's count is 7,
    # then we add 7-1=6, because 6 can be made as palindrome
    else:
        Max = max(Max, Appearances[element])
        Count += Appearances[element]-1
if Max:
    Count += 1
    print Count
else:
    print Count
