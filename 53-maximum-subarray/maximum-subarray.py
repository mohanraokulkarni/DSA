class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ls=nums
        max_sum=ls[0]
        prefix_sum=0
        for i in range(len(ls)):
            prefix_sum=prefix_sum+ls[i]

            max_sum=max(prefix_sum,max_sum)

            if prefix_sum<0:
                prefix_sum = 0
        
        return max_sum