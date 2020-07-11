#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        num_to_str_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        path = ""
        result = []
        self.dfs(num_to_str_dict, digits, path, result)
        return result

    def dfs(self, num_to_str_dict, digits, path, result):
        if digits == "":
            result.append(path)
            return
        
        for s in num_to_str_dict[digits[0]]:
            path += s
            self.dfs(num_to_str_dict, digits[1:], path, result)
            path = path[:-1]
        return

# @lc code=end

