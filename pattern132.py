class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        small = []
        small.append(nums[0])
        for i in range(1,len(nums)):
            small.append(min(nums[i],small[i-1]))
        j=len(nums)-1
        k=len(nums)
        while j>=0:
            if nums[j]>small[j]:
                while k<len(nums) and nums[k]<=small[j]:
                    k+=1
                if k<len(nums) and nums[k]<nums[j]:
                    return True
                k-=1
                if k>=0 and k<len(nums):
                    nums[k] = nums[j]
            j-=1
        return False