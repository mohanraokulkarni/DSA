class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        d= (n*(n+1)//2) - sum(nums)
        return d


        