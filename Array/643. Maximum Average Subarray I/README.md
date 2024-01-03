# <a href="https://leetcode.com/problems/maximum-average-subarray-i/description/">Maximum Average Subarray I</a>

Question Number: <a href="https://leetcode.com/problems/maximum-average-subarray-i/description/">643</a>

```
Question: Find a contiguous subarray whose length is equal to k that has the maximum average value.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
```
## Understanding the Concept
Let' use the sliding window technique to create a character window of size k. With each iteration, the window will shift forward by discarding the leftmost character and including the rightmost character, thus moving from left to right.

<!-- ### Visual Overview-->
<!-- <img src="https://github.com/alihussainia/LeetCode-Python/blob/master/Strings/1876.%20Substrings%20of%20Size%20Three%20with%20Distinct%20Characters/img/1876.gif" alt="step-by-step-visual-overview"> -->

### Code Solution
```Python3
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = sum(nums[:k])
        windowAvg = windowSum/k
        maxAvg = windowAvg

        for i in range(len(nums)-k):
            windowSum = windowSum - nums[i] + nums[i+k]
            windowAvg = windowSum/k

            maxAvg = max(maxAvg , windowAvg)

        return
```
Time Complexity: O(N-k)

Space Complexity O(1) 

Technique: Sliding Window

