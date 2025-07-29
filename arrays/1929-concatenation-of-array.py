'''
1929. Concatenation of Array
https://leetcode.com/problems/concatenation-of-array/

🎓 What I Learned:
1. If you already know how big your result will be, create the full space in 
advance instead of growing the list piece by piece.
2. Point back to the same array with .copy() to avoid creating a new one.

Time & Space: O(n) & O(n)
Revisit: No
'''

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Simple solution: 
        # return nums + nums

        # res = nums.copy()   # <- points to the same array (use .copy())
        # for num in nums:
        #     res.append(num)
        # return res

        # Sample solution (pre-allocate space) 
        n = len(nums)
        ans = [0] * (2 * n) 
        for i, num in enumerate(nums):
            ans[i] = num 
            ans[i + n] = num 
        return ans

