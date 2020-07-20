#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#

# @lc code=start
import random
class Solution:

    def __init__(self, nums: List[int]):
        self._nums = nums
        self._ori = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self._nums = self._ori[:]
        return self._nums
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        aux = self._nums[:]
        for i in range(len(self._nums)):
            idx = random.randrange(len(aux))
            self._nums[i] = aux.pop(idx)
        
        return self._nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

