class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        length=len(nums)
        max_sum=nums[0]
        pre_sum=0

        for i in range(0,length):
            num=nums[i]
            pre_sum=pre_sum+num

            max_sum=max(max_sum,pre_sum)

            if pre_sum<0:
                pre_sum=0
        
        return max_sum