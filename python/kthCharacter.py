"""
Kth Distinct String in an Array
Easy
Topics
Companies
Hint
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.

 

Example 1:

Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. 
Example 2:

Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.
Example 3:

Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".


Approach 2: Hash Set
Intuition
Our previous approach involved iterating through the array to check for duplicates, which adds a linear element to the time complexity. Let's explore a more efficient method.

In this improved approach, we'll utilize a hash set to track all encountered strings during iteration. Hash sets are ideal for this task because they offer constant-time add, remove, and lookup operations. For those unfamiliar with hash sets, the LeetCode Explore Card on hash tables provides a comprehensive overview.

We'll maintain two sets: distinctStrings and duplicateStrings. As we traverse the input array, we'll check if the current string exists in either set. If it does, we'll categorize it as a duplicate and add it to duplicateStrings. If not, we'll consider it distinct and add it to distinctStrings.

After completing the initial loop, distinctStrings will contain all unique strings. We'll then iterate through arr once more, and each time we encounter a string present in distinctStrings, we'll decrement k. When k reaches zero after a decrement, we can return that string as the kth distinct string in the array.

To illustrate the process, consider the example where arr = ["d", "b", "c", "b", "c", "a"] and k = 2. The following slideshow will demonstrate how the algorithm arrives at the solution:


Algorithm
Initialize two sets: distinctStrings to track strings that appear only once, and duplicateStrings to track strings that appear more than once.
Iterate through the array arr to populate distinctStrings and duplicateStrings:
If a string is already in duplicateStrings, skip it.
If a string is in distinctStrings, move it to duplicateStrings (indicating it is now a duplicate) and remove it from distinctStrings.
If a string is not in either set, add it to distinctStrings.
Iterate through the array arr again to find the k-th distinct string:
For each string, check if it is in duplicateStrings. If not, decrement k (indicating this string is one of the distinct strings).
When k reaches 0, return the current string as the k-th distinct string.
If no k-th distinct string is found (i.e., k does not reach 0), return an empty string.
 
"""

from typing import List


class Solution_brute_force:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        n = len(arr)
        distinct_strings = []

        # Iterate through each string in the array
        for i in range(n):
            current_string = arr[i]
            is_distinct = True

            # Check if the current string is distinct
            for j in range(n):
                if j == i:
                    continue  # Skip comparing with itself
                if arr[j] == current_string:
                    is_distinct = False
                    break

            # If the string is distinct, add it to the list
            if is_distinct:
                distinct_strings.append(current_string)

        # Check if there are enough distinct strings
        if len(distinct_strings) < k:
            return ""

        return distinct_strings[k - 1]
    
    
    ## HashSet
    class Solution:
        def kthDistinct(self, arr, k):
            distinct_strings = set()
            duplicate_strings = set()

            # First pass: Identify distinct and duplicate strings
            for s in arr:
                # If the string is already in duplicate_strings, skip further processing
                if s in duplicate_strings:
                    continue
                # If the string is in distinct_strings, it means we have seen it before,
                # so move it to duplicate_strings
                if s in distinct_strings:
                    distinct_strings.remove(s)
                    duplicate_strings.add(s)
                else:
                    distinct_strings.add(s)

            # Second pass: Find the k-th distinct string
            for s in arr:
                if s not in duplicate_strings:
                    # Decrement k for each distinct string encountered
                    k -= 1
                # When k reaches 0, we have found the k-th distinct string
                if k == 0:
                    return s

            return ""