#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/accounts-merge/

accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"]
]

# Output
# [
#     ["John", "john00@mail.com", "john_newyork@mail.com","johnsmith@mail.com"],
#     ["Mary", "mary@mail.com"],
#     ["John", "johnnybravo@mail.com"]
# ]

# accounts = [
#     ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
#     ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
#     ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
#     ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
#     ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]
# ]

# Output
# [
#     ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
#     ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
#     ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
#     ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
#     ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"]
# ]

Sets = [set(element) for element in accounts]
dontNeedIt = []
length = len(Sets)
for i in range(length):
    for j in range(i+1, length):
        Intersection = Sets[i] & Sets[j]
        for string in Intersection:
            if "@" in string:
                Sets[i] = Sets[i].union(Sets[j])
                dontNeedIt.append(j)
                break
for idx in dontNeedIt:
    del Sets[idx]

for idx, element in enumerate(Sets):
    Sets[idx] = list(element)
print Sets
