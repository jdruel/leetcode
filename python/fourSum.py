from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        
        result = []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                res = target - nums[i] - nums[j]
                left = j + 1
                right = n - 1
                while left < right:
                    if left > j + 1 and nums[left] == nums[left - 1]:
                        left += 1
                        continue
                    if right < n - 1 and nums[right] == nums[right + 1]:
                        right -= 1
                        continue
                    curr = nums[left] + nums[right]
                    if curr == res:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    elif curr < res:
                        left += 1
                    else:
                        right -= 1
        return result
    
# nums = [1,0,-1,0,-2,2]
nums = [2,2,2,2,2]
print(Solution().fourSum(nums, 8))