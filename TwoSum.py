class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}
        for i,num in enumerate(nums):
            if (target-num) in compliment:
                return [compliment[target-num], i]
            compliment[num] = i
        return []