#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for t in tasks:
            d[t] = d.get(t, 0) + 1

        total = len(tasks)
        cnt = 0
        while True:
            q = 0
            keys = sorted(d.keys(), key=lambda k: d[k], reverse=True)
            for k in keys:
                if d[k] > 0:
                    cnt += 1
                    q += 1
                    total -= 1
                    d[k] -= 1
                    if q == n + 1:
                        break

            if total == 0:
                break
            cnt = cnt + (n - q + 1 if q - 1 < n else 0)
        
        return cnt


# @lc code=end

