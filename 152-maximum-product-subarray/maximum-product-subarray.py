class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val = float('-inf')
        prefix, suffix = 1, 1

        for i in range(len(nums)):
            prefix *= nums[i]
            suffix *= nums[len(nums) - 1 - i]

            max_val = max(max_val, suffix, prefix)

            prefix = 1 if prefix == 0 else prefix
            suffix = 1 if suffix == 0 else suffix

        return max_val