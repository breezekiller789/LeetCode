#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# 用遞迴解比較好理解


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print root.val
    Inorder(root.right)


def Construct(preorder, inorder):
    if not preorder or not inorder:
        return
    root = TreeNode(preorder[0])
    index = inorder.index(root.val)  # 找出現在root的位置
    del preorder[0]                  # 最左邊可以直接刪掉因為不需要用了

    # 把左邊遞迴的結果接上去
    root.left = Construct(preorder, inorder[:index])
    # 把右邊遞迴的結果接上去
    root.right = Construct(preorder, inorder[index+1:])
    # 回傳結果
    return root


# Output: [8,5,10,1,7,null,12]
preorder = [8, 5, 1, 7, 10, 12]
inorder = sorted(preorder)
# [1, 5, 7, 8, 10, 12]

root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(7)
root.right.left = TreeNode(9)
root.right.right = TreeNode(12)
Inorder(Construct(preorder, inorder))
