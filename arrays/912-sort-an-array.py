"""
LeetCode 912: Sort An Array
https://leetcode.com/problems/sort-an-array/

📝 Summary:

🧠 Thought Process:

✅ Solution Approach:

🐞 Mistakes & Gotchas:

🎓 What I Learned:

🔁 Revisit: No
"""


# Merge sort: time and space - O(n log n) time | O(n) space. 
# We divide the array into halves log(n) times, and each merge operation takes O(n) time.
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums) 
        if length <= 1: return nums
        
        middle = length // 2
        leftArray = nums[:middle]
        rightArray = nums[middle:]

        self.sortArray(leftArray)
        self.sortArray(rightArray)
        self.merge(leftArray, rightArray, nums) 
        return nums


    def merge(self, leftArray: List[int], rightArray: List[int], array: List[int]):
        l = 0
        r = 0
        i = 0
        leftSize = len(array) // 2 
        rightSize = len(array) - leftSize 

        while l < leftSize and r < rightSize: 
            if leftArray[l] < rightArray[r]: 
                array[i] = leftArray[l]
                i += 1
                l += 1 
            else: 
                array[i] = rightArray[r]
                i += 1 
                r += 1 
        
        # leftovers 
        while l < leftSize: 
            array[i] = leftArray[l]
            i += 1 
            l += 1 
        
        while r < rightSize: 
            array[i] = rightArray[r] 
            i += 1
            r += 1 


'''
Example: [5, 2, 9, 1, 6]

- Divide: [5, 2] and [9, 1, 6]

Left: [5], [2].  l < r, so arr[0] = 5, and then leftover? [2]  -> [2, 5]
Right: [9], [1, 6].  l < r, so arr[1] = 1, and then leftover? [6]
Merge these two: 
9 > 1, so arr[0] = r[r] = 1; 9 > 6, so arr[1] = r[1] = 6. No more right size, 
so leftover 9 and we append, giving us [1, 6, 9]

Merge [2,5] and [1,6,9] 
2 > 1. arr[0] = 1 
2 < 6. arr[1] = 2 
5 > 6. arr[2] = 5 
Run out of leftsize. Leftovers: [6,9]
we append: [1,2,5,6,9] 
'''
class Solution: 
    def merge(self, leftArray, rightArray, array):
        # we use array so we have the "allocated space" needed to write it. 
        l = 0, r = 0, i = 0

        while leftArray and rightArray: 
            if leftArray[l] < rightArray[r]: 
                array[i] = leftArray[l]
                i += 1
                l += 1 
            else: 
                array[i] = rightArray[r]
                i += 1 
                r += 1 
        
        # leftovers 
        while l < len(leftArray):
            array[i] = leftArray[l]
            i += 1
            l += 1
        
        while r < len(rightArray):
            array[i] = rightArray[r]
            i += 1 
            r += 1 


        
    def mergeSort(self, nums): 
        if len(nums) <= 1: return nums
        
        leftArray = nums[:len(nums)//2]
        rightArray = nums[len(nums)//2:]

        self.mergeSort(leftArray) 
        self.mergeSort(rightArray) 

        # until we reach 1 we merge: 
        self.merge(leftArray, rightArray, nums) 
        return nums
        


    

"""
Quick example: [4,2,7] 
- Choose pivot (7)
- Partitioning: [4,2,7] -> [4,2,7]
    Why? 4 < 7. j = 0, i = 0 (no swap)
    2 < 7, j = 1, i = 1. [4,2,7]
    then swap 7 to the right position (i+1 = 2) -> [4,2,7] 
- Recursively sort left: [4,2]
    4 < 2: i = -1, j = 0 
    Then swap 2: arr[0], arr[high] swap -> [2,4]
- Combine: [2,4,7]

Quick example 2: [7,2,4]
- Choose pivot (4)
- Partitioning: [7,2,4] -> [2,4,7] 
    Why? 7 < 4. j = 0, i = -1 
    2 < 4, j = 1, i = 0. -> [2,7,4]
    then swap 4 to the right position (i+1 = 1) -> [2,4,7]
- Recursively sort left and right - [2] (base case) and [7] (base case)
- Combine: [2,4,7]
"""
# Quick sort. Time and space: O(n log n) time | O(log n) space.
# Worst case of quick sort is O(n^2) when the pivot is the smallest or largest element.
class Solution: 
    def partition(self, array, low, high):
        """
        This will return the current pivot index (the correct position), and 
        then we will recursively sort the left and right subarrays. 
        """
        pivot = array[high]  # Choose the rightmost element as pivot 
        i = low - 1    # Pointer for the small element. -1 because we haven't seen any elements yet

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1 
                array[i], array[j] = array[j], array[i]
                # Swap: array[i] with array[j]

        # Now the pivot is in the right place 
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1


    def quicksort(self, array, low=0, high=None): 
        if high is None: high = len(array) - 1

        if low < high: 
            pivotIndex = self.partition(array, low, high)
            self.quicksort(array, low, pivotIndex - 1)
            self.quicksort(array, pivotIndex + 1, high) 

        return array


