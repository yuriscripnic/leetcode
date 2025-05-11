"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. 

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.


if len(neddle) > len(haystack) return 0
char_position = 0

compare a windows of the len(neddle) with neddle startting 
char_position [0 .. postion - len(haystack) - len(neddle)] incluseive

"""


class Solution:
    ## My Solution using Window
    def strStr(self, haystack: str, needle: str) -> int:
        char_pos, hs_len, nd_len  = -1, len(haystack), len(needle)
        if not (1 <= hs_len <= 10**4 and 1 <= nd_len <= 10**4) or nd_len > hs_len:
            return -1
        final_pos = hs_len - nd_len
        while(char_pos < final_pos):
            char_pos+=1
            if haystack[char_pos: char_pos + nd_len] == needle:
                return char_pos
        return -1
    
## Similar LeetCode Solution
    def strStr_windows(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        for window_start in range(n - m + 1):
            for i in range(m):
                if needle[i] != haystack[window_start + i]:
                    break
                if i == m - 1:
                    return window_start

        return -1

##  Rabin-Karp Algorithm (Single Hash)
def strStr_RKS(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)
        if n < m:
            return -1

        # CONSTANTS
        RADIX = 26
        MOD = 1_000_000_033
        MAX_WEIGHT = 1

        for _ in range(m):
            MAX_WEIGHT = (MAX_WEIGHT * RADIX) % MOD

        # Function to compute the hash of m-String
        def hash_value(string):
            ans = 0
            factor = 1

            for i in range(m - 1, -1, -1):
                ans += ((ord(string[i]) - 97) * (factor)) % MOD
                factor = (factor * RADIX) % MOD

            return ans % MOD

        # Compute the hash of needle
        hash_needle = hash_value(needle)

        # Check for each m-substring of haystack, starting at window_start
        for window_start in range(n - m + 1):
            if window_start == 0:
                # Compute hash of the First Substring
                hash_hay = hash_value(haystack)
            else:
                # Update Hash using Previous Hash Value in O(1)
                hash_hay = (
                    (hash_hay * RADIX) % MOD
                    - ((ord(haystack[window_start - 1]) - 97) * MAX_WEIGHT)
                    % MOD
                    + (ord(haystack[window_start + m - 1]) - 97)
                    + MOD
                ) % MOD

            # If hash matches, Check Character by Character.
            # Because of Mod, spurious hits can be there.
            if hash_needle == hash_hay:
                for i in range(m):
                    if needle[i] != haystack[i + window_start]:
                        break
                if i == m - 1:
                    return window_start

        return -1
    
# Approach 3: Rabin-Karp algorithm (Double Hash)
def strStr_RK(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        if n < m:
            return -1

        # PREPROCESSING
        # longest border array
        longest_border = [0] * m
        # Length of Longest Border for prefix before it.
        prev = 0
        # Iterating from index-1. longest_border[0] will always be 0
        i = 1

        while i < m:
            if needle[i] == needle[prev]:
                # Length of Longest Border Increased
                prev += 1
                longest_border[i] = prev
                i += 1
            else:
                # Only empty border exist
                if prev == 0:
                    longest_border[i] = 0
                    i += 1
                # Try finding longest border for this i with reduced prev
                else:
                    prev = longest_border[prev - 1]

        # SEARCHING
        # Pointer for haystack
        haystack_pointer = 0
        # Pointer for needle.
        # Also indicates number of characters matched in current window.
        needle_pointer = 0

        while haystack_pointer < n:
            if haystack[haystack_pointer] == needle[needle_pointer]:
                # Matched Increment Both
                needle_pointer += 1
                haystack_pointer += 1
                # All characters matched
                if needle_pointer == m:
                    # m characters behind last matching will be window start
                    return haystack_pointer - m
            else:
                if needle_pointer == 0:
                    # Zero Matched
                    haystack_pointer += 1
                else:
                    # Optimally shift left needle_pointer.
                    # Don't change haystack_pointer
                    needle_pointer = longest_border[needle_pointer - 1]

        return -1
        
        
if __name__ == "__main__":
    print(Solution().strStr("sadbutsad","sad"))
    print(Solution().strStr("leet","leet"))
    print(Solution().strStr("leetcode","leeto"))
    print(Solution().strStr("leet","leeto"))
    print(Solution().strStr("","leeto"))
    print(Solution().strStr("leetcode",""))
    print(Solution().strStr("aa","aa"))
    print(Solution().strStr("baabbaaaaaaabbaaaaabbabbababaabbabbbbbabbabbbbbbabababaabbbbbaaabbbbabaababababbbaabbbbaaabbaababbbaabaabbabbaaaabababaaabbabbababbabbaaabbbbabbbbabbabbaabbbaa","bbaaaababa"))