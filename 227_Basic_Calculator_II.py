#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/basic-calculator-ii/

# 還有bug，因為題目的數字不一定都是個位數，有可能會有123這種，一百二十三，我的
# 程式會看成1, 2, 3


# Output: 7
s = "3+2*2"

# Output: 1
s = " 3/2 "

# Output: 5
# s = " 3+5 / 2 "


def Priority(char):
    if char == "+" or char == "-":
        return 0
    elif char == "*" or char == "/":
        return 1
    elif char == "(":
        return float("-inf")
    else:
        return -1


def TellMeWhatThatIs(s, index, length):
    # 如果是左括號，代表右手邊一定馬上接著一個數字，不可能會是運算子，同時左邊
    # 一定是一個運算子，不可能是數字，檢查時小心越界

    # 先把在邊界的都解決，後面才比較好處理，如果剛好在頭，肯定是左括號，剛好在尾
    # 就肯定是右括號
    if index == 0:
        return "("
    elif index == length - 1:
        return ")"

    # 會來這裡就一定不會站在邊界上。
    if s[index+1].isdigit() or not s[index-1].isdigit() or s[index-1].isspace():
        return "("
    else:
        return ")"


postfix = ""
stack = []
length = len(s)
for i, char in enumerate(s):
    if char.isdigit():
        postfix += char
        continue

    # Determine what this space actually is
    if char.isspace():
        continue
        # 我下面原本是以為空白是左括號右括號的意思，結果好像不是，這邊就是在
        # handle這些情況
        # char = TellMeWhatThatIs(s, i, length)
        # if char == ")":
        #     while stack and stack[-1] != "(":
        #         postfix += stack.pop()
        #     stack.pop()
        #     continue
        # else:
        #     stack.append(char)
        #     continue

    if stack and Priority(char) > Priority(stack[-1]):
        stack.append(char)
        continue
    elif stack and Priority(char) <= Priority(stack[-1]):
        while stack and Priority(char) <= Priority(stack[-1]):
            postfix += stack.pop()
        stack.append(char)
    else:
        stack.append(char)

while stack and stack[-1] != "(":
    postfix += stack.pop()

# Evaluate value
for char in postfix:
    if char.isdigit():
        stack.append(char)
        continue
    value2 = int(stack.pop())
    value1 = int(stack.pop())
    if char == "+":
        stack.append(value1+value2)
    elif char == "-":
        stack.append(value1-value2)
    elif char == "*":
        stack.append(value1*value2)
    elif char == "/":
        stack.append(value1/value2)
print stack[-1]
