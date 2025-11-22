from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        for i in range(n - 2, -1, -1):
            if nums[i] == 0:
                continue
            min_step = min(nums[i], n - i - 1)
            for step in range(1, min_step + 1):
                if dp[i + step]:
                    dp[i] = True
                    break
        return dp[0]
    
    def canJump2(self, nums: List[int]) -> bool:
        max_reach = 0
        n = len(nums)
        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= n - 1:
                return True
        return True
    

nums = [2,3,1,1,4]
print(Solution().canJump2(nums))  # Output: True