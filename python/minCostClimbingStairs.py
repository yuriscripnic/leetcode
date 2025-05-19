"""
Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

if:
    climb 1 step dp(i) = dp(i-1)+ n(i)
    climb 2 steps dp(i) = min(dp(i-1)+ n(i), dp(i-2)+ n(i))

base case
dp(0) = n[0]
dp(1) = min (n[0],n[1])



Tabulation
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        // The array's length should be 1 longer than the length of cost
        // This is because we can treat the "top floor" as a step to reach
        int minimumCost[] = new int[cost.length + 1];
        
        // Start iteration from step 2, since the minimum cost of reaching
        // step 0 and step 1 is 0
        for (int i = 2; i < minimumCost.length; i++) {
            int takeOneStep = minimumCost[i - 1] + cost[i - 1];
            int takeTwoSteps = minimumCost[i - 2] + cost[i - 2];
            minimumCost[i] = Math.min(takeOneStep, takeTwoSteps);
        }
        
        // The final element in minimumCost refers to the top floor
        return minimumCost[minimumCost.length - 1];
    }
}

Recursion
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minimum_cost(i):
            # Base case, we are allowed to start at either step 0 or step 1
            if i <= 1:
                return 0

            # Check if we have already calculated minimum_cost(i)
            if i in memo:
                return memo[i]

            # If not, cache the result in our hash map and return it
            down_one = cost[i - 1] + minimum_cost(i - 1)
            down_two = cost[i - 2] + minimum_cost(i - 2)
            memo[i] = min(down_one, down_two)
            return memo[i]

        memo = {}
        return minimum_cost(len(cost))

"""

class Solution:
    def minCostClimbingStairs(self, n: int) -> int:
        
        def dp(i:int)-> int:
            if i == steps:
                return 0
            
            if i <=1:
                return min(n[0],n[1])
            
            return n[i] + min(dp(i+1), dp(i+2))
        
        steps= len(n)
        return dp(0)                
            
if __name__ == "__main__":    
    print(Solution().minCostClimbingStairs([10,15,20])) # 15
    print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])) # 6