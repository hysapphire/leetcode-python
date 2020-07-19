#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        cnt = 0
        ab_dict = {}
        for a in A:
            for b in B:
                ab_dict[a+b] = ab_dict.get(a+b, 0) + 1
        
        for c in C:
            for d in D:
                if -(c+d) in ab_dict:
                    cnt += ab_dict[-(c+d)]

        return cnt


        # cnt = 0
        # a_dict = {}
        # b_dict = {}
        # c_dict = {}
        # d_dict = {}
        # for a in A:
        #     a_dict[a] = a_dict.get(a, 0) + 1
        # for b in B:
        #     b_dict[b] = b_dict.get(b, 0) + 1
        # for c in C:
        #     c_dict[c] = c_dict.get(c, 0) + 1
        # for d in D:
        #     d_dict[d] = d_dict.get(d, 0) + 1

        # ab_dict = {}
        # cd_dict = {}
        # for a in a_dict:
        #     for b in b_dict:
        #         ab_dict[a+b] = ab_dict.get(a+b, 0) + a_dict[a] * b_dict[b]

        # for c in c_dict:
        #     for d in d_dict:
        #         cd_dict[c+d] = cd_dict.get(c+d, 0) + c_dict[c] * d_dict[d]

        # for ab in ab_dict:
        #     if -ab in cd_dict:
        #         cnt = cnt + ab_dict[ab] * cd_dict[-ab]
        
        # return cnt
        
# @lc code=end

