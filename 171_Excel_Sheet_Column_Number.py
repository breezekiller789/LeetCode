#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/excel-sheet-column-number/

# 26進位，查表而已沒什麼

Table = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
         'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
         'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
         'Z': 26}
# columnTitle = "A"
# columnTitle = "AB"
columnTitle = "ZY"
# columnTitle = "FXSHRXW"
columnTitle = columnTitle[::-1]

Sum = 0
for idx in xrange(len(columnTitle)-1, -1, -1):
    Sum += pow(26, idx) * Table[columnTitle[idx]]
print Sum
