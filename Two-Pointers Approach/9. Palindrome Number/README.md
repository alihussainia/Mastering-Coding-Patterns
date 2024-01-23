# <a href="https://leetcode.com/problems/palindrome-number/">9. Palindrome Number</a>

Question Number: <a href="https://leetcode.com/problems/palindrome-number/">9</a>

```
Question: Given an integer x, return true if x is a palindrome, and false otherwise..

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
```
## Understanding the Concept
Let' convert x into a string and use the Two Pointer technique to traverse it.

### Code Solution - Optimized Approach
```Python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)

        left = 0
        right = len(x) - 1

        while left < right:
            if x[left] != x[right]:
                return False
            else:
                left += 1
                right -= 1

        return True
```
Technique: Two Pointer Approach


