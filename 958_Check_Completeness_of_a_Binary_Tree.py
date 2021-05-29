#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

# 我的方法就是level order traversal，我要把每一個level的點都放進一個陣列，
# 依照順序的放，最後我再當中有沒有中間空掉一個然後後面還有值，如果有這種情況，這
# 顆樹就不會是complete，因為complete的話他的NULL pointer一定都是堆在後面，不會在
# 中間跑出來，但是程式寫起來挺複雜，是因為我要去handle一些edge case，像是skewed的
# 這種樹，如果他一直往左，我程式就會一直變肥，會一直放空指標，為了要cover這些就要
# 多做一些檢查。


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def LevelOrder(root):
    Q = [root]
    Level = 0
    result = []
    while Q:
        childCount = pow(2, Level)
        count = 0
        tmpList = [0] * childCount  # 這用來放每一個level的node值，包含空指標
        while count < childCount:
            currentNode = Q.pop(0)
            # 如果空的，就append兩個空兒子進去queue裡面然後繼續。
            if not currentNode:
                Q.append(None)
                Q.append(None)
                tmpList[count] = None
                count += 1
                continue
            # 這一行是要解決歪斜樹，如果有任何點他的左兒子空的，但是右兒子卻有東
            # 西這樣代表這一定不是Complete
            if not currentNode.left and currentNode.right:
                return False
            tmpList[count] = currentNode.val    # 放現在節點的值進去tmp list
            Q.append(currentNode.left)   # 左兒子放進去，即便是空的，也給他放
            Q.append(currentNode.right)  # 右兒子也是，不管空不空都給他放
            count += 1

        # 走到這裡代表我們已經放完現在這一層所有節點，接下來還是要檢查這一層是
        # 不是合法的，就tmp list走一次，如果有發現None在中間冒出來，那就不是合法
        hasValue = False    # 這個flag代表我們tmp list有沒有不是None的
        for element in tmpList:
            if element is not None:
                hasValue = True
                break
        # 有值就進去
        if hasValue:
            # 如果裡面有值，但是我目前result最後面是None代表說我有None在中間冒出
            # 來，這代表不合法，回傳False
            if result and result[-1] is None:
                return False
            result.extend(tmpList)
        # 沒有值代表這一層全都是空的，就把累積到現在的result傳回去讓driver檢查。
        else:
            return result
        Level += 1
    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
result = LevelOrder(root)
# 如果result傳回來是False代表這是有問題的，就回傳False
if not result:
    print False
    exit()

# 檢查剛剛result是不是合法的
for i, num in enumerate(result[:-1]):
    if num is None and result[i+1] is not None:
        print False
        exit()
print True
