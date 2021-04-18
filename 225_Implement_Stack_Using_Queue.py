#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/implement-stack-using-queues/


class MyStack(object):
    def __init__(self):
        self.Queue = []
        self.elements = 0

    def push(self, x):
        self.Queue.append(x)
        self.elements += 1

    def pop(self):
        for i in range(self.elements-1):
            item = self.Queue[0]
            self.Queue.append(item)
            del self.Queue[0]
        item = self.Queue[0]
        del self.Queue[0]
        self.elements -= 1
        return item

    def top(self):
        if self.elements == 0:
            return None
        return self.Queue[-1]

    def empty(self):
        return self.elements == 0


Stack = MyStack()
Stack.push(12)
Stack.push(3)
Stack.push(7)
Stack.push(1)
Stack.push(5)
print Stack.pop()
print Stack.pop()
print Stack.pop()
print Stack.pop()
print Stack.pop()
print Stack.top()
print Stack.empty()
