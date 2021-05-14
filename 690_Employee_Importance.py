#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/employee-importance/

# 用遞迴解，不難。


# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
        """
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        """
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


def EmployImportance(employees, id):
    Sum = 0
    for employee in employees:
        # Enter this if matches the id
        if employee.id == id:
            Sum += employee.importance
            # Use recursion to calculate the importance
            for subordinate in employee.subordinates:
                Sum += EmployImportance(employees, subordinate)
            return Sum


employees = []
employees.append(Employee(1, 5, [2, 3]))
employees.append(Employee(2, 3, []))
employees.append(Employee(3, 3, []))
id = 1
print EmployImportance(employees, id)
