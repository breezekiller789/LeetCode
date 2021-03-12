# https://leetcode.com/problems/reverse-integer/
# ======================Code==========================

value = input()
# 這個while loop就是先把後面的零清掉，就一直除以10就好了，因為反轉之後零不用。
while value % 10 == 0 and value != 0:
    value /= 10
# 如果一開始小於零，反轉之後也要小於零，所以正數、負數要分開處理，負數多一個"-"
if value < 0:
    ans = "-" + str(value)[:0:-1]
else:
    ans = str(value)[::-1]

# 反轉之後的數，不可以overflow，如果overflow就直接印0
if int(ans) > 1 << 31:
    print 0
elif int(ans) <= -1 << 31:
    print 0
else:
    print int(ans)
