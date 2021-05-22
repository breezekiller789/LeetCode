#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import heapq

# https://leetcode.com/problems/design-search-autocomplete-system/


class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.Strings = [[] for _ in range(27)]
        self.currentString = ""
        for i, string in enumerate(sentences):
            prefix = string[0]
            if prefix == " " or " " in string:
                self.Strings[-1].append((-times[i], string))
            if prefix != " ":
                self.Strings[ord(prefix)-ord("a")].append((-times[i], string))
        print self.Strings

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == "#":
            string = self.currentString
            prefix = self.currentString[0]
            if prefix == " " or " " in string:
                for i, element in enumerate(self.Strings[-1]):
                    if element[1] == string:
                        self.Strings[-1][i] = (element[0]-1, string)
                        break
                else:
                    self.Strings[-1].append((-1, string))
            if prefix != " ":
                for i, element in enumerate(self.Strings[ord(prefix)-ord("a")]):
                    if element[1] == string:
                        self.Strings[ord(prefix)-ord("a")][i] = (element[0]-1,
                                                                 string)
                        break
                else:
                    self.Strings[ord(prefix)-ord("a")].append((-1, string))
            self.currentString = ""
            print self.Strings
            return []

        # Store the character and return the Top 3 string in the specific heap
        self.currentString += c
        if c == " ":
            self.Strings[-1].sort()
            ret = []
            for element in self.Strings[-1][:3]:
                ret.append(element[1])
            return ret
        else:
            self.Strings[ord(c)-ord("a")].sort()
            ret = []
            for element in self.Strings[ord(c)-ord("a")][:3]:
                ret.append(element[1])
            return ret
        # return self.TopThreeString(c)

    # def addString(self, string, time):
    #     # add the string to our data structure
    #     prefix = string[0]
    #     if prefix == " " or " " in string:
    #         self.Strings[-1].append((time, string))
    #     if prefix != " ":
    #         self.Strings[ord(prefix)-ord("a")].append((time, string))

    # def TopThreeString(char):
    #     self.Strings[ord(char)-ord("a")].sort()
    #     ret = []
    #     for element in self.Strings[ord(char)-ord("a")][-3:]:
    #         ret.append(element[1])
    #     return ret


obj = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"],
                         [5, 3, 2, 2])
print obj.input("i")
print obj.input(" ")
print obj.input("a")
print obj.input("#")
