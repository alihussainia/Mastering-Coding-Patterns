class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = sum(nums[:k])
        windowAvg = windowSum/k
        maxAvg = windowAvg

        for i in range(len(nums)-k):
            windowSum = windowSum - nums[i] + nums[i+k]
            windowAvg = windowSum/k

            maxAvg = max(maxAvg , windowAvg)

        return maxAvg
