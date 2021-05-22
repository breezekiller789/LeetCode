#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

# https://leetcode.com/problems/guess-the-word/

# 這一題真的很特別，是leetcode上面很少出現的互動式題目，這一題我是直接看討論區
# 的大神分享，這個方法不一定每次都ＡＣ，但是ＡＣ機率很高，方法就是，亂猜！但是亂
# 猜也不是隨便在亂猜，我們每一次亂猜，得到配對是0的機率非常非常高，是(25/26)^6，
# 接近80%，所以我們不用妄想一次猜中，我們每猜一次，就把我們wordlist中，也跟我們
# 現在猜的字串match個數一樣的，我們都直接不要用，因為如果我們現在猜出去的字串是
# match 0，然而，我拿這個字串去跟我所有word list的字串比，如果也是match 0的，我
# 們也可以保證這個字串肯定也不是答案，所以可以不用去看了，而這樣，我們可以每一次
# 就大大縮減我們的字串個數，猜對答案的機率就越來越高，這一題的概念就是這樣，當然
# 還有另外一種方法叫做minimax，那個太複雜了我就不記了，但是方法好像看起來差不多，
# 而且我現在這個方法我覺得超級屌超級聰明，但是並不是完美是真的。


class Master(object):
    def __init__(self, secret, maxGuess):
        self.secret = secret
        self.maxGuess = 10
        self.guessCount = 0

    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        if self.guessCount == self.maxGuess:
            print "Max Guess Exceeded"
            exit()
        if word == self.secret:
            print "Bingo!"
            exit()
        Count = 0
        for i, char in enumerate(word):
            if char == self.secret[i]:
                Count += 1
        self.guessCount += 1
        return Count if Count < 6 else "Bingo!"


class Solution(object):

    def __init__(self):
        self.haha = 0

    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        self.haha = 0
        for i in range(10):
            guess = random.choice(wordlist)
            x = master.guess(guess)
            wordlist = [w for w in wordlist
                        if sum(i == j for i, j in zip(guess, w)) == x]


master = Master("hbaczn", 10)
wordlist = [
    "gaxckt", "trlccr", "jxwhkz", "ycbfps", "peayuf", "yiejjw",
    "ldzccp", "nqsjoa", "qrjasy", "pcldos", "acrtag", "buyeia",
    "ubmtpj", "drtclz", "zqderp", "snywek", "caoztp", "ibpghw",
    "evtkhl", "bhpfla", "ymqhxk", "qkvipb", "tvmued", "rvbass",
    "axeasm", "qolsjg", "roswcb", "vdjgxx", "bugbyv", "zipjpc",
    "tamszl", "osdifo", "dvxlxm", "iwmyfb", "wmnwhe", "hslnop",
    "nkrfwn", "puvgve", "rqsqpq", "jwoswl", "tittgf", "evqsqe",
    "aishiv", "pmwovj", "sorbte", "hbaczn", "coifed", "hrctvp",
    "vkytbw", "dizcxz", "arabol", "uywurk", "ppywdo", "resfls",
    "tmoliy", "etriev", "oanvlx", "wcsnzy", "loufkw", "onnwcy",
    "novblw", "mtxgwe", "rgrdbt", "ckolob", "kxnflb", "phonmg",
    "egcdab", "cykndr", "lkzobv", "ifwmwp", "jqmbib", "mypnvf",
    "lnrgnj", "clijwa", "kiioqr", "syzebr", "rqsmhg", "sczjmz",
    "hsdjfp", "mjcgvm", "ajotcx", "olgnfv", "mjyjxj", "wzgbmg",
    "lpcnbj", "yjjlwn", "blrogv", "bdplzs", "oxblph", "twejel",
    "rupapy", "euwrrz", "apiqzu", "ydcroj", "ldvzgq", "zailgu",
    "xqpsr", "wxdyho", "alrplq", "brklfk"
]
obj = Solution()
print obj.findSecretWord(wordlist, master)
