#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        total = len(t)
        t_dict = {}
        for tt in t:
            if tt in t_dict:
                t_dict[tt] += 1
            else:
                t_dict[tt] = 1

        s_dict = {}
        cnt = 0
        min_len = 1e6
        start = 0
        min_s = -1
        min_e = -1
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1

            if s[i] in t_dict and s_dict[s[i]] <= t_dict[s[i]]:
                    cnt += 1
            if cnt == total:
                while s[start] not in t_dict or s_dict[s[start]] > t_dict[s[start]]:
                    s_dict[s[start]] -= 1
                    start += 1
                if i - start + 1 < min_len:
                    min_len = i - start + 1
                    min_s = start
                    min_e = i

        return s[min_s:min_e+1]

# @lc code=end

