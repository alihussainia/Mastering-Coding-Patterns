class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        windowSum = sum(arr[:k])
        windowAvg = windowSum / k
        if windowAvg >= threshold:
            count=1
        else:
            count=0

        for i in range(len(arr)-k):
            windowSum = windowSum - arr[i] + arr[i+k]
            windowAvg = windowSum / k
            if windowAvg >= threshold:
                count+=1
        return count
