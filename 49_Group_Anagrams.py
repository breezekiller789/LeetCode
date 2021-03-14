#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/group-anagrams/

# 未解完，有點誤解題目，他是要整個的字母重排，包含重複的，我以為用集合來解，這樣
# 就不包含重複的哭啊

# 測資
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# strs = ["a"]
# strs = ["", "b", ""]
strs = ["ac", "c"]


kill_List = []  # 放那些組成字母一樣的人，每一次iteration就要刪掉
count = 0       # 來算總共有幾組集合
Ans = []        # 答案，回傳用
brothers = []   # 拿來放組成字母一樣的
idx = 0

# 從頭抓第一個，往後面比，用集合來做，集合的交集如果和原本一樣，代表字母都一樣。
while idx < len(strs):
    word = strs[idx]
    # 一進來的第一個一定有，直接加進兄弟list
    # brothers.append(word)
    for jdx, element in enumerate(strs[idx:]):
        # 兩個集合交集跟element一樣代表完全一樣，小心不可以寫成跟word一樣，因為
        # 有可能word是element的子集合，例如word={"eat"}, element={"eaten"}，這樣
        # 他們的組成字元不一樣。
        if set(word) == set(element):
            kill_List.append(element)
            brothers.append(element)
    count += 1
    Ans.append(brothers[:])
    # 把字母一樣的那些人都刪掉
    for victim in kill_List:
        strs.remove(victim)

    # print strs, idx, word, kill_List
    if not kill_List:
        idx += 1
    # 把kill list跟brothers重新刷新
    del kill_List[:], brothers[:]
for i in Ans:
    print i
