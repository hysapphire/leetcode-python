#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if n == 0:
        #     return [""]
        # if n == 1:
        #     return ["()"]
        
        # result = []
        # for i in range(0, n):
        #     for a in self.generateParenthesis(i):
        #         for b in self.generateParenthesis(n - 1 - i):
        #             result.append("(" + a + ")" + b)
        
        # return result
        result = []
        path = ""
        self.dfs(n, 0, 0, path, result)
        return result
    
    def dfs(self, n, left, right, path, result):
        if left == n:
            for _ in range(n - right):
                path += ")"
            result.append(path)
            for _ in range(n - right):
                path = path[:-1]
            return
        
        path += "("
        self.dfs(n, left + 1, right, path, result)
        path = path[:-1]

        if left > right:
            path += ")"
            self.dfs(n, left, right + 1, path, result)
            path = path[:-1]





# @lc code=end

