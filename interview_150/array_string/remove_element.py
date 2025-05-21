class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for i in range(len(nums)):
            if nums[i] == val:
                counter += 1
            else:
                nums[i - counter] = nums[i]
        for _ in range(counter):
            nums.pop()