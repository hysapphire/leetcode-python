#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = []
        d = {}
        for i in range(len(s) - 9):
            d[s[i:i+10]] = d.get(s[i:i+10], 0) + 1
        
        for k, v in d.items():
            if v > 1:
                result.append(k)
        
        return result

# @lc code=end

