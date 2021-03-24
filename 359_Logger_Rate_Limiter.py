#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/logger-rate-limiter/


class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Log_Info = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp,
        otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.Log_Info:
            self.Log_Info[message] = timestamp + 10
            return True
        if timestamp < self.Log_Info[message]:
            return False
        else:
            self.Log_Info[message] = timestamp + 10
            return True


obj = Logger()
print obj.shouldPrintMessage(1, "foo")
print obj.shouldPrintMessage(2, "boo")
print obj.shouldPrintMessage(3, "goo")
print obj.shouldPrintMessage(4, "foo")
print obj.shouldPrintMessage(11, "foo")
print obj.shouldPrintMessage(13, "foo")
