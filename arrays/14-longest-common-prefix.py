"""
LeetCode 14: Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/


✅ Solution Approach:
- Deal with edge cases first: empty list or list with empty string
- Iterate through each position and then each string 
- If any string does not match the first string at that position, return the result so far
- If all strings match at that position, add the character to the result
- Return the result after checking all positions

🐞 Mistakes & Gotchas:
- Index out of bounds
- Forgot edge cases


🎓 What I Learned:
- What's the shortest input? Use the shortest string length to limit the iteration
- Handle edge cases like empty lists or strings
- Which "for" comes first: the one that remains constant.
- Use a "standard string" (usually the first) for comparison.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or "" in strs:
            return ""
        if len(strs) == 1: 
            return strs[0]

        res = ""
        # Iterate each string 
        # Iterate each position/character. 
        # Position outside. Check position of EACH character 
        for i in range(0, min(len(s) for s in strs)): 
            # First string ok. If second string is longer, the common prefix would not 
            # Exceed length of the first string 
            for word in strs: 
                if word[i] != strs[0][i]: 
                    return res 
            res += word[i]
    
        # Return res if no mismatch
        return res