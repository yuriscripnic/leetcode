"""
House Robber

Solution
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each
of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

***
If you don't rob a house, then your current ammount of money is just for the last house  $ = dp(i-1) ,
If you rob this house you ammount of money is the current house value plus the value from the house n-2, $=  dp(i-2) + num(i)

dp(i) = max (dp(i-1), dp(i-2) + nums[i])

base cases
dp(0) = nums[0]
dp(1) = max(nums[0], nums[1])


T = S = O(n)

"""

from typing import List


class Solution:
    def rob_top_bottom(self, nums: List[int]) -> int: # recursion & hashmap
        def dp(i):
            if i==0:
                return nums[0]
            if i==1:
                return max(nums[0], nums[1])
            if i not in memo:
                memo[i] = max(dp(i-1), dp(i-2) + nums[i])
            return memo[i]
        memo={}
        return dp(len(nums)-1)
    
    def rob_bottom_top(self, nums: List[int]) -> int: # iteration & list
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]
            
    
        
        
        
if __name__ == "__main__":
    print(Solution().rob_top_bottom([1,2,3,1])) # 4
    print(Solution().rob_top_bottom([2,7,9,3,1])) #12
    print(Solution().rob_top_bottom([2,1])) # 2
    
    print(Solution().rob_bottom_top([1,2,3,1])) # 4
    print(Solution().rob_bottom_top([2,7,9,3,1])) #12
    print(Solution().rob_bottom_top([2,1])) # 2
    