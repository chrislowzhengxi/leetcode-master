"""
LeetCode 169: Majority Element
https://leetcode.com/problems/majority-element/

📝 Summary:

🧠 Thought Process:

✅ Solution Approach:

🐞 Mistakes & Gotchas:

🎓 What I Learned:
1. The Boyer-Moore Voting Algorithm is an efficient way to find the majority element in linear time and constant space.
2. The key insight is that the majority element will always "win" against any other candidate due to its frequency.

🔁 Revisit: No
"""

# Fastest: Boyer-Moore - O(n) and O(1) 
# Intuition: you choose a candidate. If you see it again, you increment a count. If you see a different one, you 
# decrement the count. When it hits 0, you choose a new candidate.
# Why this works: The majority element must appear more than half the time, so it will always "win" against any other candidate.
# The majority will always be the last candidate standing. (even if it drops to 0 sometimes)
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = 0
        for num in nums: 
            if count == 0: 
                candidate = num     
            count += 1 if num == candidate else -1 
        return candidate

# My solution: 
# Space and time: O(n) for both
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Hash? Loop through it and get the count? 
        hashtable = {}
        for num in nums: 
            hashtable[num] = 1 + hashtable.get(num, 0)
            if hashtable[num] > (len(nums) / 2): 
                return num





