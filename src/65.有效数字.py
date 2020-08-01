#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:
            return False
        
        i = 0
        j = len(s) - 1
        while i < len(s) - 1 and s[i] == " ":
            i += 1
        while j > 0 and s[j] == " ":
            j -= 1

        if i > j:
            return False
        
        s = s[i:j+1]

        numSeen = False
        dotSeen = False
        eSeen = False
        for i in range(len(s)):
            if ord("0") <= ord(s[i]) <= ord("9"):
                numSeen = True
            elif  s[i] == ".":
                if dotSeen or eSeen:
                    return False
                dotSeen = True
            elif s[i] == "E" or s[i] == "e":
                if eSeen or not numSeen:
                    return False
                eSeen = True
                numSeen = False
            elif s[i] == "+" or s[i] == "-":
                if i != 0 and s[i-1] != "e" and s[i-1] != "E":
                    return False
            else:
                return False

        return numSeen

# @lc code=end

