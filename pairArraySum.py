"""
Array Partition
Easy
Topics
Companies
Hint
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

 

Example 1:

Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
Example 2:

Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
 

Constraints:

1 <= n <= 104
nums.length == 2 * n
-104 <= nums[i] <= 104


Overview
We are given a list of 2N integers. We need to group these integers into N pairs such that the sum of minimum elements in all pairs is the maximum possible.

The key observation here is that if we have a pair like (a,b) such that a≤b, then we will add a to the answer and b cannot be used anymore. Therefore, in each such pair, we will add the value of the smaller element but the greater element will not contribute to the answer.

Suppose x is the smallest possible element in the given list. This means that the contribution to the answer for any pair that includes x must be x, irrespective of the paired element. The other element will essentially be wasted. Hence to minimize our losses, we would like to pair x with the smallest element other than x.

The number paired with x will be the second smallest element in the given list. Hence, we will pair each element with the closest unpaired number in ascending sorted order. After sorting the given list, the first element can be paired with the second element, the third element can be paired with the fourth, and so on.


Approach 1: Sorting
Intuition

We will sort the given list using the built-in sorting function. In the sorted list we will pair the first two elements then the next two elements and so on. Therefore, the first element (at index 0) will be added to the answer maxSum as it is the minimum of the first two elements. Similarly, the third element in the list (at index 2) will be added, and so on. Hence, we will only sum the elements located at the even indices.

Algorithm

Sort the list nums.
Initialize the answer variable maxSum as 0.
Iterate over the list nums and add the elements at even indices to maxSum.
Return maxSum.

"""



from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the list in ascending order
        nums.sort()
        # Initialize sum to zero
        max_sum = 0
        for i in range(0, len(nums), 2):
            # Add every element at even positions (0-indexed)
            max_sum += nums[i]
            
        return max_sum 