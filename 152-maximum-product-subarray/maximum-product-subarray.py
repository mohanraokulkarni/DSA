class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # If the list is empty, return 0 (though the input guarantees at least one number)
        if not nums:
            return 0

        maxp = float('-inf')  # Start with the smallest possible value

        # Left-to-right and right-to-left traversal
        mul_l = mul_r = 1  # Initialize left and right products
        
        length = len(nums)
        for i in range(length):
            # Left-to-right product
            mul_l = mul_l * nums[i] if mul_l != 0 else nums[i]
            # Right-to-left product
            mul_r = mul_r * nums[length - 1 - i] if mul_r != 0 else nums[length - 1 - i]

            # Track maximum product from both directions
            maxp = max(maxp, mul_l, mul_r)

        return maxp
