from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        closest = abs(target - res)
        for i in range(len(nums) - 2):
            # if nums[i] >= target:
            #     return res
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(target - sum)
                if diff < closest:
                    closest = diff
                    res = sum
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    return sum
        return res

# nums = [-1,2,1,-4]
nums = [-100,-98,-2,-1]
print(Solution().threeSumClosest(nums, -101))  # Output: 2