# 136. Single Number
#
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.
#
#
#
# Example 1:
#
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
#
# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:
#
# Input: nums = [1]
# Output: 1
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 1 XOR 1 or 0 XOR 0 = 0
        # 1 XOR 0 or 0 XOR 1 = 1

        n = nums[0]
        for i in nums[1:]:
            n ^= i
        return n
