# https://leetcode.com/problems/longest-increasing-subsequence/description/
# difficulty: medium
# topics: array, binary search, dynamic programming

# problem:
# Given an integer array nums, return the length of the longest strictly increasing subsequence.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length
        for i in range(1, length):
            greatest = 0
            for j in range(i):
                if nums[i] > nums[j]: greatest = max(greatest, dp[j])
            dp[i] += greatest
        return max(dp)
# bottom-up
# time complexity: O(n^2)
# space complexity: O(n)

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        
        def dp(i, prevHighest):
            if i == length: return 0
            if nums[i] <= prevHighest: return dp(i+1, prevHighest)
            return max(dp(i+1, nums[i])+1, dp(i+1, prevHighest))
        
        return dp(0, -float("inf"))
"""
# top-down
