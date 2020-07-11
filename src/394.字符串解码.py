#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        ans = ""
        for ss in s:
            if ss.isdigit():
                num = num * 10 + int(ss)
            elif ss == "[":
                stack.append((num, ans))
                num = 0
                ans = ""
            elif ss == "]":
                n, a = stack.pop()
                ans = a + n * ans
            else:
                ans += ss
        
        return ans



    #     return self.dfs(s, 0)[0]

    # def dfs(self, s, i)
        # num = 0
        # ans = ""
        # while i < len(s):
        #     if s[i].isdigit():
        #         num = num * 10 + int(s[i])
        #     elif s[i] == "[":
        #         ss, i = self.dfs(s, i + 1)
        #         ans += ss * num
        #         num = 0
        #     elif s[i] == "]":
        #         return ans, i
        #     else:
        #         ans += s[i]
            
        #     i += 1
        
        # return ans, i

# @lc code=end

