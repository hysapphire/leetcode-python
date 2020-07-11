#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#

# @lc code=start
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(set)
        weight = defaultdict()
        for equation, value in zip(equations, values):
            graph[equation[0]].add(equation[1])
            graph[equation[1]].add(equation[0])
            weight[tuple(equation)] = value
            weight[(equation[1], equation[0])] = 1.0 / value
        
        def dfs(start, end, visited):
            if (start, end) in weight:
                return weight[(start, end)]

            if start not in graph or end not in graph:
                return 0
            
            if start in visited:
                return 0
            
            visited.add(start)

            res = 0
            for tmp in graph[start]:
                res = dfs(tmp, end, visited) * weight[(start, tmp)]
                if res != 0:
                    weight[(start, end)] = res
                    break
            visited.remove(start)

            return res

        result = []
        for query in queries:
            tmp = dfs(query[0], query[1], set())
            if tmp == 0:
                tmp = -1.0
            result.append(tmp)
        
        return result

# @lc code=end

