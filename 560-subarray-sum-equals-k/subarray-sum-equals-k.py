class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_upto_dict={0:1}
        prefix_sum=0
        count=0
        
        for i in range(0,len(nums)):
            prefix_sum=prefix_sum+nums[i]

            diff= prefix_sum-k

            if diff in sum_upto_dict:
                #left=sum_upto_dict[diff]
                count=count+ sum_upto_dict[diff]
            
            if prefix_sum not in sum_upto_dict:
                sum_upto_dict[prefix_sum]=1
            else:
                sum_upto_dict[prefix_sum]=sum_upto_dict[prefix_sum]+1 

        
        return count


        