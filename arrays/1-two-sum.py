"""
LeetCode 1: Two Sum
https://leetcode.com/problems/two-sum/

🧠 Thought Process:
    # nums, target
    # [3,2,4], target = 6
    # {"3": 0, "2": 1, "4": 2}. At 4, we check if 6 - 4 = 2 exists in the hashmap.

🎓 What I Learned:
- "in" in dictionary checks for key existence, not value.

🔁 Revisit: Yes
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # Brute force approach
        # for i in range(0, len(nums)-1): 
        #     for j in range(i+1, len(nums)): 
        #         if nums[i] + nums[j] == target: 
        #             return [i,j]
            
        
        # Hashmap approach: time complexity O(n), space complexity O(n)

        hashmap = {}
        for i, num in enumerate(nums): 
            leftover = target - num 
            if leftover in hashmap: 
                return [hashmap[leftover],i]
            hashmap[num] = i













