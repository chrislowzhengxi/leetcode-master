'''
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

🎓 What I Learned:
1. Using the set() function removes all the non-unique elements from a list.
2. HashSets are useful for checking membership in O(1) time. (i.e. O(n) time for the whole list))

Time & Space: O(n) & O(n)  
Revisit: No
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ## sorting: O(nlogn), O(1)/O(n)
        # nums.sort()
        # for i in range(1, len(nums)): 
        #     if nums[i] == nums[i - 1]: 
        #         return True
        # return False

        ## Using sets length
        # return len(set(nums)) != len(nums) 

        # Using sets 
        ans = set() 
        for num in nums: 
            if num in ans: 
                return True
            ans.add(num) 
        return False

        

