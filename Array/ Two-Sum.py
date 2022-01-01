class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {} 
        for index, val in enumerate(nums):
            diff = target-val # logic -> diff + val = target
            if diff in hMap:
                return [prevMap[diff],index]
            hMap[val]=index # else add val:index into hMap

# Reference: NeetCode