# <a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/">Two Sum II - Input Array Is Sorted</a>

Question Number: <a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/">167</a>

```
Question: Given a sorted array of numbers, find out which two numbers sum is equal to target number.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
```
## Understanding the Concept
Let' use the two pointer technique to solve this question!

### Code Solution
```Python3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            twoSum = numbers[left] + numbers[right]

            if twoSum == target:
                return [left+1,right+1]

            elif twoSum < target:
                left+=1
            
            else:
                right-=1
```
Time Complexity: O(N)

Space Complexity O(1) 

Technique: Two Pointer Approach

