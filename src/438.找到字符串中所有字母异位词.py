#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = {}
        window = {}
        for pp in p:
            need[pp] = need.get(pp, 0) + 1
        
        result = []
        left = 0
        right = 0
        valid = 0
        while right < len(s):
            ss = s[right]
            right += 1

            if ss in need:
                window[ss] = window.get(ss, 0) + 1
                if window[ss] == need[ss]:
                    valid += 1
            
            while right - left >= len(p):
                if valid == len(need.keys()):
                    result.append(left)
                
                ss = s[left]
                left += 1
                if ss in need:
                    if window[ss] == need[ss]:
                        valid -= 1
                    window[ss] -= 1
        
        return result
            


        # p_dict = {}
        # for pp in p:
        #     p_dict[pp] = p_dict.get(pp, 0) + 1
        
        # p_len = len(p)

        # result = []
        # i = 0
        # while i < len(s) - p_len + 1:
        #     d = p_dict.copy()
        #     is_matched = True
        #     for j in range(i, i + p_len):
        #         if s[j] in d:
        #             d[s[j]] -= 1
        #             if d[s[j]] < 0:
        #                 is_matched = False
        #                 while s[i] != s[j]:
        #                     i += 1
        #                 break
        #         else:
        #             is_matched = False
        #             i = j
        #             break
        #     if is_matched:
        #         result.append(i)
        #     i += 1
            
        # return result 
            
# @lc code=end

