
#     Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:

# Input: s = "loveleetcode"

# Output: 2

# Example 3:

# Input: s = "aabb"

# Output: -1

 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.

"""
create an ordereddict char_map 
create set char_already_seen

for each s char in s
    if s is not in already_seen
        if s isnot in char_map
            add s and idx to char_map
            add s to already seen
        if s is in charmap remove it from charmap
    if charmap len is 0 return -1
    return the value of the first charmap key
"""


from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = OrderedDict()
        already_seen = []
        for idx, c in enumerate(s): 
            if c not in already_seen:
                already_seen.append(c)
                if c not in char_map:       
                    char_map[c] = idx
                else:
                    del char_map[c]
            else:
               if c in char_map:
                   del char_map[c] 
        if len(char_map) > 0:
            return char_map[next(iter(char_map))]
        else:
            return -1
        
        

if __name__ == "__main__":
    print(Solution().firstUniqChar("leetcode"))
    print(Solution().firstUniqChar("loveleetcode"))
    print(Solution().firstUniqChar("aabb"))
    print(Solution().firstUniqChar("aadadaad"))