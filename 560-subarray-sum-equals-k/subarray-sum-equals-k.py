class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ls=nums
        target=k
        d={0:1}
        count=0


        prefix_sum=0
        for i in range(0,len(ls)):
            prefix_sum=prefix_sum+ls[i]
            
            diff=prefix_sum-target
            
            if diff in d:
                count=count+d[diff]
            if prefix_sum not in d:
                d[prefix_sum]=1
            else:
                d[prefix_sum]=d[prefix_sum]+1
            
            
        return count
        
        
        
    
    


        