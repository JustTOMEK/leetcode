class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        temp = nums[:len(nums) - k]
        temp2 = nums[len(nums) - k:]
        nums[:k] = temp2
        nums[k:] = temp

