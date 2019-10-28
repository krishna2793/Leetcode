class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums)
        i = 0
        while i<last:
            if nums[i] == val:
                last -=  1
                nums[i] = nums[last]
            if nums[i] != val:
                i += 1
        return last