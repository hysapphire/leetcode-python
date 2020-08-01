#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        word_list = path.split("/")
        
        for word in word_list:
            if not word or word == ".":
                continue

            if word == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(word)

        s = ""
        for word in stack:
            s += "/"
            s += word
        if not s:
            s = "/"
        
        return s

        # stack = []
        # s = 0
        # dot_cnt = 0
        # has_word = False
        # for i in range(len(path)):
        #     if path[i] == "/":
        #         if has_word:
        #             stack.append(path[s:i])
        #             has_word = False
        #         s = i + 1
        #         dot_cnt = 0
        #     elif path[i] == ".":
        #         if has_word:
        #             stack.append(path[s:i])
        #             has_word = False
        #         s = i + 1
        #         dot_cnt += 1
        #         if dot_cnt == 2 and stack:
        #             stack.pop()
        #             dot_cnt = 0
        #     else:
        #         has_word = True
        
        # s = ""
        # for word in stack:
        #     s += "/"
        #     s += word
        # if not s:
        #     s = "/"
        
        # return s

# @lc code=end

