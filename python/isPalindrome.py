"""
Valid Palindrome

Solution
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 10**5
s consists only of printable ASCII characters.

s= lower(s) pos_begin = 0 pos_end = len(s) -1
remove no char and space from s
while pos_start > pos_end compare each a pos_begin with pos_end

pos_begin == pos_end return True
if clean_str[pos_start] != clean_str[pos_end] return false
    else pos_start +1 pos_end -1
return True
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not (1 <= len(s) <= 2 * 10**5):
            return False

        clean_str = ""
        for c in s:
            if c.isalnum() and (not c.isspace()):
                clean_str+= c.lower()
        print(f"[{clean_str}]")
        
        if len(clean_str) == 0:
            return True
        
        pos_begin, pos_end = 0, len(clean_str) -1
            
        
        while(pos_begin <= pos_end):   
            if clean_str[pos_begin] != clean_str[pos_end]:
                return False
            
            if pos_begin == pos_end:
                return True
            
            pos_begin+=1
            pos_end-=1

        return True
    
    ## LeetCode reversed string
    def isPalindrome_reversed_string(self, s: str) -> bool:

        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list
            
        
        
if __name__ == "__main__":
    
    print(Solution().isPalindrome( "A man, a plan, a canal: Panama")) # True
    print(Solution().isPalindrome( "abcde")) # False
    print(Solution().isPalindrome( "race a car")) # False
    print(Solution().isPalindrome("0P")) # False
    print(Solution().isPalindrome("")) # True
    print(Solution().isPalindrome("a")) # True
    print(Solution().isPalindrome("!@#$%^&*()_+ ,.<>?;:\"\'[]{}\\|")) # True