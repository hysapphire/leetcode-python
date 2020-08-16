#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for ss, tt in zip(s, t):
            if ss not in d1:
                d1[ss] = tt
            else:
                if d1[ss] != tt:
                    return False
            
            if tt not in d2:
                d2[tt] = ss
            else:
                if d2[tt] != ss:
                    return False
        
        return True

# @lc code=end

