# <a href="https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/">Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold</a>

Question Number: <a href="https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/">1343</a>

```
Question: Count averages of the subarrays of size k that are equal or greater than threshold.

Example 1:
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3

Example 2:
Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
```
## Understanding the Concept
Let' use the sliding window technique to create a character window of size k. With each iteration, the window will shift forward by discarding the leftmost character and including the rightmost character, thus moving from left to right. In the beginning, we will calculate the sum of first k elements and then their average and finally will check whether the average is greater or equal to the threshold. Then we will use a for-loop to traverse through second element till len(arr)-kth index element (we used len(arr)-k to avoid index out of bound error). Then we will use the first windowSum and will remove the ith element as well as add the i+kth element to it. This way we will not need to calcualte the sum of elements that we already calculated before, thus making us efficient. Finally, we will update the count variable if we will find the windowAvg greater than the threshold. At last, we will return the count as our output.

### Code Solution
```Python3
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        windowSum = sum(arr[:k])
        windowAvg = windowSum/k
        if windowAvg >= threshold:
            count=1
        else:
            count=0

        for i in range(len(arr)-k):
            windowSum = windowSum - arr[i] + arr[i+k]
            windowAvg = windowSum/k
            if windowAvg >= threshold:
                count+=1

            return count
```
Time Complexity: O(N-k)

Space Complexity O(1) 

Technique: Sliding Window


