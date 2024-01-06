# <a href="https://leetcode.com/problems/find-all-anagrams-in-a-string/description/">Find All Anagrams in a String</a>

Question Number: <a href="https://leetcode.com/problems/find-all-anagrams-in-a-string/description/">438</a>

```
Question: Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Note: An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

In Simple Words: Return the first indices of those substrings of size k which can form string "P".

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
```
## Understanding the Concept
Let' use the sliding window technique to create a character window of size k. In this approach, we will use hashmaps rather sorted strings along with knife approach where we will remove the preceding character before jumping to the next one.

### Visual Overview
<img src="https://github.com/alihussainia/LeetCode-Python/blob/master/Strings/1876.%20Substrings%20of%20Size%20Three%20with%20Distinct%20Characters/img/1876.gif" alt="step-by-step-visual-overview">

### Code Solution - Optimized Approach
```Python3
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        res = []
        p_counter = Counter(p) 
        window_counter = Counter(s[:k]) 

        if p_counter == window_counter:
            res.append(0)

        for i in range(len(s)-k): 
            window_counter[s[i]] -= 1

            if window_counter[s[i]]==0:
                del window_counter[s[i]]

            window_counter[s[i+k]] += 1

            if window_counter == p_counter:
                res.append(i+1)
        
        return res
```
Time Complexity: O((len(s)-k)*k)

Space Complexity O(k) 

Technique: Sliding Window


