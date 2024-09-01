class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s=[]
        for i in range(0,len(nums)):
            diff=target-nums[i]
            k=nums[i+1:]
            if diff in k:
                h=k.index(diff)
                s.append(i)
                s.append(h+i+1)
        return s

            
        