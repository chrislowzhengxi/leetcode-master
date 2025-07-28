"""
LeetCode 228: Summary Ranges
https://leetcode.com/problems/summary-ranges/

📝 Summary:
Given sorted list of unique integers, a->b ranges for consecutive. 

🧠 Thought Process:
- Start, end
- Iterated through the list. If there is a match, increment end. 
- Else, we append the range to the answer list and reset start and end.

✅ Solution Approach:
- Time Complexity: O(n) — where n is the length of the input list.
- Space Complexity: O(1) - excluding the output list 


🐞 Mistakes & Gotchas:
1. Moved i every time. Made it more complicated. 
2. Restarting start and end. I have no idea what to do. 

🎓 What I Learned:
- Only move i when CONDITION is met. Will make it easier to reset start and end.
- Reset start and end: keep track of i. If you incremented it, i+1 would not be the next number. 

🔁 Revisit:
Yes
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []: 
            return []
        i = 0
        answer = [] 
        start, end = nums[i], nums[i]
        while i < (len(nums) - 1): ## and something 
            if nums[i+1] != (nums[i] + 1):
                if start == end: 
                    answer.append(str(nums[i]))
                else:
                    answer.append(f"{start}->{end}")
                # Reset indices
                start = nums[i+1]
                end = nums[i+1]
            else: 
                end = nums[i+1]
            i += 1

        if start == end:
            answer.append(str(start))
        else:
            answer.append(f"{start}->{end}")

        return answer 
    



# algomap.io solution
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []     
        i = 0 
        
        while i < len(nums): 
            start = nums[i]  
            while i < len(nums)-1 and nums[i] + 1 == nums[i + 1]: 
                i += 1 
            
            if start != nums[i]: 
                ans.append(str(start) + "->" + str(nums[i]))
            else: 
                ans.append(str(nums[i]))
            
            i += 1
 
        return ans