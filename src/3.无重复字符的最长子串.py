#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        right = 0
        window = {}
        while right < len(s):
            ss = s[right]
            right += 1
            window[ss] = window.get(ss, 0) + 1

            while window[ss] > 1:
                window[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left)
        
        return max_len


        # max_len = 0
        # start_pos = 0
        # pos_dict = {}
        # for idx, ss in enumerate(s):
        #     if ss in pos_dict:
        #         start_pos = max(pos_dict[ss] + 1, start_pos)
        #     max_len = max(max_len, idx - start_pos + 1)
        #     pos_dict[ss] = idx
        #     # if ss not in pos_dict or pos_dict[ss] < start_pos:
        #     #     max_len = max(max_len, idx - start_pos + 1)
        #     # else:
        #     #     start_pos = pos_dict[ss] + 1
        #     # pos_dict[ss] = idx

        # return max_len
# @lc code=end

