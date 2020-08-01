#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        splited_words = []
        s = []
        cnt = 0
        for word in words:
            t = cnt + len(word)
            if t > maxWidth:
                splited_words.append(s)
                s = [word]
                cnt = len(word) + 1
            else:
                s.append(word)
                cnt = t + 1
        
        splited_words.append(s)

        res = []
        for splited_word in splited_words[:-1]:
            s = ""
            if len(splited_word) == 1:
                num_space = 0
            else:
                num_space = (maxWidth - sum([len(word) for word in splited_word])) // (len(splited_word) - 1)
            delta_num_space = (maxWidth - sum([len(word) for word in splited_word])) - (len(splited_word) - 1) * num_space
            
            if len(splited_word) == 1:
                s = ""
                s += splited_word[0]
                for _ in range(delta_num_space):
                    s += " "
            else:
                for word in splited_word[:-1]:
                    s += word
                    for _ in range(num_space):
                        s += " "
                    if delta_num_space > 0:
                        s += " "
                        delta_num_space -= 1

                s += splited_word[-1]
            res.append(s)
        
        s = ""
        for word in splited_words[-1][:-1]:
            s += word
            s += " "
        s += splited_words[-1][-1]
        for _ in range(maxWidth - len(s)):
            s += " "
        
        res.append(s)

        return res

# @lc code=end

