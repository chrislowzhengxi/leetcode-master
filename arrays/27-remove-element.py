"""
LeetCode 27: Remove Element
https://leetcode.com/problems/remove-element/

📝 Summary:

🧠 Thought Process:

✅ Solution Approach:
Time and Space: O(n) time, O(1) space

🐞 Mistakes & Gotchas:
Was trying to find a "swap candidate". 

🎓 What I Learned:
1. You DO NOT need to search for the last valid element every time. You can just keep 
shrinking your second pointer, j, as you go.
2. You can use i<=j as a loop condition to avoid unnecessary swaps.

🔁 Revisit: No
"""



# Correct solution: 
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return i


# 3 2 2 3; i, j = 0, 3
# 3 2 2 3; i, j = 0, 2
# 2 2 2 3; i, j = 0, 1 
# 2 2 2 3; i, j = 1, 1 
# i, j = 1,2 


"""
val = 2
i, j = 0, 7
0 1 2 2 3 0 4 2 

i, j = 1, 7
i, j = 2, 7
Swap no change 
i, j = 2, 6
0 1 4 2 3 0 4 2 
i, j = 2, 5
i, j = 3, 5
0 1 4 0 3 0 4 2
i, j = 3, 4
i, j = 4, 4
i, j = 5, 4 break 
"""



# Neetcode 
# You overwrite the non-equal ones to the front, ignoring the equal ones. Increment k which are the ones that remain 
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k



# Wrong:
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Two pointers. One goes through nums. The other one keeps track of the val. 
        If equals to the val, you move it to the back (and slide the rest to the front) 
        process until you reach len. (Use pop?)
        """
        # 3 2 2 3 
        i = 0    # first 
        j = len(nums) - 1    # last 
        res = len(nums)
        while i < len(nums) and j >= 0:  # M: i keeps swapping even after exceeding j 
            if nums[i] == val:
                while nums[j] == val:    # M: index error 
                    j -= 1 
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp 
                res -= 1  
            i += 1     # M: unconditional 
        return res 
                



            