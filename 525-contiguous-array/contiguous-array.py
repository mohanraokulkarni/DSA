class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        d={0:-1}
        prefix_sum=0
        max_length=0

        for i in range(0,len(nums)):
            if nums[i]==0:
                prefix_sum=prefix_sum - 1
            else:
                prefix_sum=prefix_sum + 1
            
            if prefix_sum in d:
                left=d[prefix_sum]
                rang=i-left
                max_length=max(max_length,rang)
            else:
                d[prefix_sum] = i
        return max_length
        