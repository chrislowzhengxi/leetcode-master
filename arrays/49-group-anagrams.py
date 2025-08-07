"""
LeetCode 49: Group Anagrams
https://leetcode.com/problems/group-anagrams/

📝 Summary:
Given an array of strings, group the anagrams together. An anagram is a word formed by rearranging the letters of another, such as "eat" and "tea".

🧠 Thought Process:
They have the same character count so we can use a dictionary to map it.

✅ Solution Approach: 
1. Create a master dictionary to hold the sorted character tuples as keys and lists of anagrams as values.
2. For each string, create a character count dictionary.
3. Convert the character count dictionary to a sorted tuple to use as a key.
4. If the key exists in the master dictionary, append the string to the list; otherwise
, create a new list with the string.
5. Finally, return the values of the master dictionary as a list of lists.

🐞 Mistakes & Gotchas:
1. I have no idea how the tuple sorted works.
2. Data structures are complex. Return dict_values you need to convert it to a list.

🎓 What I Learned:
1. Tuples can be used as keys in dictionaries because they are immutable, but not lists.
2. Convert dict.values() to a list to avoid type errors when returning.

3. Use ord for unicode character mapping.

🔁 Revisit: No
"""

# Time complexity: O(n * k log k), where n is the number of strings and k is the maximum length of a string.
# Space complexity: O(n * k), where n is the number of strings and k is the maximum length of a string.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_dict1 = []
        # edge cases: ["a"] return it alone [["a"]], same for [[""]]
        # Loop through the whole thing 

        master_dict = {} 

        # {e: 1, a: 1, t: 1}: eat, {e: 1, a: 1, t: 1}: tea ... 
        for s in strs: 
            dict1 = {}
            for char in s: 
                dict1[char] = 1 + dict1.get(char, 0) 
            # sort the dictionary (so eat and tea has a, e, t) 
            dict1 = tuple(sorted(dict1.items()))
            
            # Unhashable type, list; Lists cannot be a key (hash) because it is mutable 
            if dict1 not in master_dict: 
                master_dict[dict1] = [s]
            else: 
                master_dict[dict1].append(s) 
        
        # Change to list: otherwise you return dict_values and type error 
        return list(master_dict.values())
    


# More efficient approach
# Time: O(n * k), where n is the number of strings and k is the maximum length of a string.
# (because for c in s is O(k) worst case)
# Space: O(n * k), where n is the number of strings and k is the maximum length of a string.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s: 
                count[ord(c) - ord('a')] += 1
                # e.g. e becomes 4 (5th letter, 4th index) 
                # Now we have a list, which is not hashable, so we use a tuple
                res[tuple(count)].append(s) 
        return list(res.values())

"""
We will have a list of: 
e.g. (1, ... , 1, ..., 1, ...): eat, ate, where the ones are indices 0, 19, 4
"""

    
