#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        result = []
        self.dfs(s, 0, path, result)
        return result

    def is_valid(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def dfs(self, s, idx, path, result):
        if idx > len(s) - 1:
            result.append(path[:])
            return
        
        for i in range(idx, len(s)):
            if self.is_valid(s[idx:i+1]):
                self.dfs(s, i + 1, path + [s[idx:i+1]], result)
# @lc code=end

