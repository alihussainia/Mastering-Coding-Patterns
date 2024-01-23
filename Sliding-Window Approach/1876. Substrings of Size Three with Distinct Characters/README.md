# <a href="https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/">Substrings of Size Three with Distinct Characters</a>

Question Number: <a href="https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/">1876</a>

```
Question: A string is good if there are no repeated characters.
Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
A substring is a contiguous sequence of characters in a string.

Example 1:
Input: s = "xyzzaz"
Output: 1

Example 2:
Input: s = "aababcabc"
Output: 4
```
## Understanding the Concept
Let' use the sliding window technique to create a character window of size 3. With each iteration, the window will shift forward by discarding the leftmost character and including the rightmost character, thus moving from left to right.

### Visual Overview
<img src="https://github.com/alihussainia/LeetCode-Python/blob/master/Strings/1876.%20Substrings%20of%20Size%20Three%20with%20Distinct%20Characters/img/1876.gif" alt="step-by-step-visual-overview">

### Code Solution
```Python3
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)  
        for i in range(n - 2):
            if len(set(s[i:i + 3])) == 3:
                count += 1 
        return count
```
Time Complexity: O(N)

Space Complexity O(1) 

Technique: Sliding Window

