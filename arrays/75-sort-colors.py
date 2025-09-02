"""
LeetCode 75: Sort Colors
https://leetcode.com/problems/sort-colors/

📝 Summary:

🧠 Thought Process:

✅ Solution Approach:

🐞 Mistakes & Gotchas:

🎓 What I Learned:
You need a copy of the original array to avoid overwriting values while sorting.
For three pointers: What is a Dutch national flag problem? It is a problem of sorting 
an array of three distinct values (like 0, 1, 2) using three pointers to partition the
array into three sections.

🔁 Revisit: No
"""

# Counting sort: time and space - O(n + k), O(k)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def countsort():
            largest = max(nums) 

            count = [0] * (largest+1)    # [2, 2, 2] 

            for num in nums: 
                count[num] += 1 
            
            # Prefix 
            for i in range(1, len(count)):    #[2, 4, 6]
                count[i] += count[i-1]
            
            nums2 = nums.copy() 
            for i in range(len(nums) - 1, -1, -1):
                val = nums2[i]
                nums[count[val] - 1] = val 
                count[val] -= 1
    
    
        countsort()



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 3 pointers 
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i,j):
            tmp = nums[i] 
            nums[i] = nums[j] 
            nums[j] = tmp 

        while i <= r: 
            # Two conditions: when nums is 0 and nums is 2 (that is when we swap). 
            # If we have nums = 0, we can just shift the i pointer to the next one (because the swapped is definitely 1. we safely skip)
            # If we have nums = 2 we need to check i again, because it can be 0 or 1. we don't want to skip the 0. 
            if nums[i] == 0: 
                swap(l, i) 
                l += 1 
            elif nums[i] == 2: 
                swap(r, i)
                r -= 1 
                i -= 1
            i += 1 


        
        