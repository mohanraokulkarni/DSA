class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        d=set(nums)
        for i in range(0,n+1):
            if i not in d:
                return i


        