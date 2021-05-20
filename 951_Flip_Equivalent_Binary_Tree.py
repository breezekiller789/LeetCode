#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/flip-equivalent-binary-trees/


class Solution(object):
    def flipEquiv(self, root1, root2):

        def FlipEquivalent(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return FlipEquivalent(root1.left, root2.left) and \
                FlipEquivalent(root1.right, root2.right) \
                or FlipEquivalent(root1.left, root2.right) and \
                FlipEquivalent(root1.right, root2.left)
        return FlipEquivalent(root1, root2)


obj = Solution()
obj.flipEquiv(None, None)
