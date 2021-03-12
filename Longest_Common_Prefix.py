# https://leetcode.com/problems/longest-common-prefix/
strs = ["flower", "flow", "flight"]
ans = ""

# 想法就是，我就直接抓第一個字串來操刀，拿著第一個字元下去後面的字串裡面看看是不
# 是在第零個位置，如果是才繼續，如果不是，代表當中有字串沒有這個prefix，就直接跳
# 出來，然而，我就直接拿第一個字串的字元下去比，一次就append上去到ans這個變數裡
# 如果該字元都是大家的prefix，我就再拿下一個字元，加上去，再做一次，舉個例，以上
# 面這個例子，我一開始就拿flower的'f'字元，放到ans裡，此時ans = "f"，然後下去後面
# 的字串比看看有沒有是prefix，如果是，就再抓下一個字元，ans = "fl"，再下去比，
# 比到有人不具有這個prefix，像是最後就會停在ans = "flo"的時候，因為"flight"沒有這
# 個prefix，所以就會跳出來，然而最後多出了那個"o"，就直接把它拿掉就好，所以就
# ans[0:-1]
if len(strs) == 0:
    print ans
    exit()
for i, char in enumerate(strs[0]):
    ans += char
    for j, word in enumerate(strs[1:]):
        # print ans, char, word, word.find(char)
        if word.find(ans) == -1 or word.find(ans) != 0:
            print ans[0:-1]
            exit()
print ans
