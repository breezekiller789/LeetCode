#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/my-calendar-i/


# Got AC, but slow
class MyCalendar(object):

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.calendar:
            self.calendar.append((start, end))
            return True
        self.calendar.append((start, end))
        self.calendar.sort()
        for idx, interval in enumerate(self.calendar[:-1]):
            if interval[1] > self.calendar[idx+1][0]:
                if interval == (start, end):
                    del self.calendar[idx]
                else:
                    del self.calendar[idx+1]
                return False
        return True


obj = MyCalendar()
print obj.book(10, 20)
print obj.book(15, 25)
print obj.book(20, 30)
print obj.book(28, 40)
