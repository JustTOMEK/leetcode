class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = [1] * n
        product = 1
        for i in range(0, n):
            products[i] *= product
            product *= nums[i]

        product = 1
        for i in range(n - 1, -1, -1):
            products[i] *= product
            product *= nums[i]
        return products

