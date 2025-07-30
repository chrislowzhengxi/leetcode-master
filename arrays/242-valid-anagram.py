'''
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/

🎓 What I Learned:
1. Use hash table to count occurrences of characters in both strings. Efficient lookup and insertion.
2. What are hash tables? Hash tables are data structures that map keys to values, allowing for fast data retrieval.

Time & Space: O(n+m) & O(1)
Revisit: No
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        # Set? Hash table?
        dict1 = {}
        dict2 = {} 
        for word in s: 
            dict1[word] = 1 + dict1.get(word,0)
            # if word not in dict1: 
            #     dict1[word] = 1 
            # else: 
            #     dict1[word] += 1 
        
        for word in t: 
            dict2[word] = 1 + dict2.get(word, 0) 
            # if word not in dict2: 
            #     dict2[word] = 1 
            # else: 
            #     dict2[word] += 1 
        
        return dict1 == dict2 

        # a: 2; n: 1, g: 1, r: 1, m: 1  (if the same it's true)
        # Sample: use get(s[i], 0). If doesn't show up, then add the key/value as 0.