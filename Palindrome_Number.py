# https://leetcode.com/problems/palindrome-number/
# ===========================Code==============================

x = raw_input()
x = str(x)
if x == x[::-1]:
    print "true"
else:
    print "false"
