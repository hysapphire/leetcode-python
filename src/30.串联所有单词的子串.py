#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_word = len(words)
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1

        res = []
        for i in range(len(s) - word_len * num_word + 1):
            m = dict(d)
            flag = True
            for j in range(num_word):
                word = s[i + j * word_len : i + j * word_len + word_len]
                if m.get(word, 0) > 0:
                    m[word] -= 1
                else:
                    flag = False
                    break
            if flag:
                res.append(i)

        return res

# @lc code=end

