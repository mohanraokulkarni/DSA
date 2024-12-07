class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=len(nums)
        i=0
        k=0
        g=[]
        while i<(l-k):
            if nums[i] == 0:
                h=nums.pop(i)
                k=k+1
                g.append(h)
            else:
                i+= 1
        while g:
            nums.append(0)
            g.pop(0)
        return nums
