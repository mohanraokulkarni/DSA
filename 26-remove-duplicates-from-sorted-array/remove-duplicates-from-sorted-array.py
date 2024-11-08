class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set()
        j=0
        l=len(nums)
        for i in range(l):
            if nums[i] not in s:
                s.add(nums[i])
                nums[j]=nums[i]
                j+=1
                continue

            
        return j