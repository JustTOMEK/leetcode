class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_set = set()
        counter = 0
        for i in range(len(nums)):
            if nums[i] not in nums_set:
                nums_set.add(nums[i])
                nums[counter] = nums[i]
                counter += 1
        return counter