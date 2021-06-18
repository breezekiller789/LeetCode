#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Output: 9
# Explanation: ((2 + 1) * 3) = 9
tokens = ["2", "1", "+", "3", "*"]

# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# tokens = ["4", "13", "5", "/", "+"]

# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

stack = []
for token in tokens:
    print stack
    if token[-1].isdigit():
        stack.append(int(token))
    else:
        num1 = stack.pop()
        num2 = stack.pop()
        if token == "+":
            stack.append(num2+num1)
        elif token == "-":
            stack.append(num2-num1)
        elif token == "*":
            stack.append(num2*num1)
        elif token == "/":
            if num1 * num2 < 0:
                stack.append(abs(num2)/abs(num1)*-1)
            else:
                stack.append(num2/num1)
print stack[0]
