#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        path = []
        result = []
        self.dfs(s, path, result, 0)
        return result

    def dfs(self, s, path, result, idx):
        if len(path) == 3:
            t = int(s[idx:])
            if (0 < t <= 255 and s[idx] != "0") or (t == 0 and len(s[idx:]) == 1):
                result.append(str(path[0]) + "." + str(path[1]) + "." + str(path[2]) + "." + s[idx:])
            return
        
        for i in range(idx + 1, len(s)):
            t = int(s[idx:i])
            if (0 < t <= 255 and s[idx] != "0") or (t == 0 and i == idx + 1):
                self.dfs(s, path + [t], result, i)
            else:
                return

# @lc code=end

