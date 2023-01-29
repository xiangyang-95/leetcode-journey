#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            remain = target - num
            if remain in seen:
                return [seen[remain], i]
            else:
                seen[num] = i
                
# @lc code=end

