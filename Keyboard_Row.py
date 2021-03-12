# https://leetcode.com/problems/keyboard-row/
set1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R',
        'T', 'Y', 'U', 'I', 'O', 'P'}
set2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'A', 'S', 'D', 'F', 'G',
        'H', 'J', 'K', 'L'}
set3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'}
words = ["Hello", "Alaska", "Dad", "Peace"]
ans = []
# 想法很簡單，就用離散的集合論來解，把input的字串搞成set，然後把他去跟三個row的
# 集合做intersection，如果交集之後還是input set，就代表這個字串在該row裡面。
for word in words:
    target_set = set(word)
    if target_set & set1 == target_set:
        ans.append(word)
    elif target_set & set2 == target_set:
        ans.append(word)
    elif target_set & set3 == target_set:
        ans.append(word)

print ans
