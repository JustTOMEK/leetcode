class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        len_nums = len(nums)
        left = 0
        right = 0
        minimum_len = len_nums + 1
        current_sum = nums[0]
        while right < len_nums:
            if current_sum >= target:
                if right - left <= minimum_len:
                    minimum_len = right - left
                current_sum -= nums[left]
                left += 1
                if left == len_nums:
                    break
            else:
                right += 1
                if right == len_nums:
                    break
                current_sum += nums[right]
        if minimum_len == len_nums + 1:
            return 0
        else:
            return minimum_len + 1