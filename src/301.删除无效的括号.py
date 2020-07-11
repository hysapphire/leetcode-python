#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = 0
        right = 0
        for ss in s:
            if ss == "(":
                left += 1
            elif ss == ")":
                if left == 0:
                    right += 1
                else:
                    left -= 1
        
        result = []
        path = ""
        self.dfs(s, path, result, left, right, 0, 0, 0)
        return set(result)


    def dfs(self, s, path, result, left, right, lcnt, rcnt, idx):
        if rcnt > lcnt or left < 0 or right < 0:
            return
        if len(s) == idx:
            if lcnt == rcnt:
                result.append(path)
            return
        
        if s[idx] != "(" and s[idx] != ")":
            path += s[idx]
            self.dfs(s, path, result, left, right, lcnt, rcnt, idx + 1)
        else:
            if s[idx] == "(":
                lcnt += 1
            else:
                rcnt += 1

            path += s[idx]
            self.dfs(s, path, result, left, right, lcnt, rcnt, idx + 1)
            path = path[:-1]

            if s[idx] == "(":
                left -= 1
                lcnt -= 1
            else:
                right -= 1
                rcnt -= 1

            self.dfs(s, path, result, left, right, lcnt, rcnt, idx + 1)

# @lc code=end

