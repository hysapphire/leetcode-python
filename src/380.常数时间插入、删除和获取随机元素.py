#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] 常数时间插入、删除和获取随机元素
#

# @lc code=start
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._list = []
        self._dict = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self._dict:
            return False
        
        self._dict[val] = len(self._list)
        self._list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self._dict:
            return False
        
        last_val = self._list[-1]
        idx = self._dict[val]

        self._list[-1], self._list[self._dict[val]] = self._list[self._dict[val]], self._list[-1]
        self._dict[last_val] = idx
        
        self._dict.pop(self._list[-1])
        self._list.pop()

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self._list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
