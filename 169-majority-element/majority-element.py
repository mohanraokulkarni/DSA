class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=len(nums)
        if l==1:
            return nums[0]
        f=dict()
        d=0
        for i in range(0,l):
            if nums[i] not in f:
                f[nums[i]] = 1
            else:
                f[nums[i]]=f[nums[i]]+1
                if f[nums[i]] > l//2:
                    d=nums[i]
        return d