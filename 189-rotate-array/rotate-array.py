class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ls=[]
        n=len(nums)
        
        for i in range(0,k):
            d=nums.pop(n-1)
            nums.insert(0,d)
        
        print(nums)
        