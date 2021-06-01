#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/decode-ways/

# Still have some bugs, but i'm very close

# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12)
s = "12"

# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or
# "BBF" (2 2 6)
# s = "226"

# Output: 0
# Explanation: There is no character that is mapped to a number starting with 0.
# The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of
# which start with 0.
# Hence, there are no valid ways to decode this since all digits need to be
# mapped
# s = "0"

# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero
# ("6" is different from "06")
# s = "06"

hashTable = dict()
for i in range(1, 27):
    hashTable[str(i)] = chr(i-1 + ord("A"))

# dp[i][j] -> s[i~j] decode ways

length = len(s)
dp = [[0 for _ in range(length)] for _ in range(length)]
for i in range(length-1, -1, -1):
    dp[i][i] = 0
    for j in range(i+1, length):
        if s[i:j+1] in hashTable:
            dp[i][j] = dp[i+1][j] + 2
        else:
            if s[i] == "0":
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = dp[i+1][j] + 1
print dp[0][length-1]
