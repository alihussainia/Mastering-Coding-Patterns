# <a href="https://leetcode.com/problems/move-zeroes/">Move Zeroes</a>

### Question Number: <a href="https://leetcode.com/problems/move-zeroes/">283</a>

```
Question: Given a sorted array of numbers, find out which two numbers sum is equal to target number.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
```
### Technique: `Two-Pointer`

### Difficulty Level: `Easy`

### Code Solution
```Python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0

        for p2 in range(len(nums)):
            if nums[p2] != 0:
                nums[p1],nums[p2] = nums[p2], nums[p1]

                p1+=1
```
### Complexities:

`Time Complexity: O(N)`

`Space Complexity O(1)`
