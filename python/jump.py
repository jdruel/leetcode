from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n - 1
        jump = 0
        jump_max = 0
        tmp_jump_max = 0
        for i in range(n):
            if jump_max >= n - 1:
                return jump
            elif i > jump_max:
                jump += 1
                jump_max = tmp_jump_max
            tmp_jump_max = max(tmp_jump_max, i + nums[i])
        return jump
    

# nums = [2,3,1,1,4]
nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
print(Solution().jump(nums))