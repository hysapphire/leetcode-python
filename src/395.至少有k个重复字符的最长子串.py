#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] 至少有K个重复字符的最长子串
#

# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        t = min(set(s), key=s.count)
        if s.count(t) >= k:
            return len(s)
        
        return max(self.longestSubstring(a, k) for a in s.split(t))

# @lc code=end
