# from typing import List

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sum = 0
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:], start=i+1):
                if a+b == target:
                    return [i, j]
        return []

    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i, a in enumerate(nums):
            value = target - a
            if value in map:
                return [map[value], i]
            map[a] = i
        return []
    

solver = Solution()
print(solver.twoSum([2,7,11,15], 9))      # 输出 [0, 1]
print(solver.twoSum2([2,7,11,15], 9))     # 输出 [0, 1]