#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            t = "".join(sorted(s))
            if t not in d:
                d[t] = [s]
            else:
                d[t].append(s)
        
        return list(d.values())
            
# @lc code=end