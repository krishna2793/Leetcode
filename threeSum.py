class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        #print(nums)
        N = len(nums)
        for i in range(N-1):
            l = i+1
            r = N-1
            if i>0 and nums[i]==nums[i-1]: continue
            while l<r:
                tot = nums[i]+nums[l]+nums[r]
                #print(i,l,r,tot)
                if tot == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif tot>0:
                    r -= 1
                else:
                    l += 1
        return ret